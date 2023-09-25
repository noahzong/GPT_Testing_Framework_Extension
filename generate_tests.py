from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

import argparse
import glob
import itertools
import json
import os.path
import sys

from llm_test_helpers import get_llm, get_args
args = get_args(sys.argv)
llm = get_llm(args.model)

# Test generation prompt
raw_prompt = json.loads(open("config.json").read())["prompt"]
prompt = PromptTemplate.from_template(raw_prompt)

for function in itertools.chain(glob.glob("functions/*.py")):
    if "__init__" in function:
        continue

    filename = function.replace("functions/", "").replace(".py", "")
    if os.path.isfile(f"tests/test_{filename}.py"):
        print(f"Skipping {filename}, test already exists.")
        continue

    # Get code and create prompt
    print(f"Generating test for {function}.")
    with open(function) as f:
        code = f.read()
    code_prompt = prompt.format(code=code)
    
    # Generate tests and clean up output
    output = llm.predict(code_prompt)
    output = output.replace("```python", "").replace("```py", "").replace("```", "").strip()
    output = f"from functions.{filename} import {filename}\n" + output

    # Write out final code
    with open(f"tests/test_{filename}.py", "w") as f:
        f.write(output)