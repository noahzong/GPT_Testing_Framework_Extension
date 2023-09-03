from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

import glob
import itertools

# Swap out with whatever model you'd like to test
llm = OpenAI()
# Test generation prompt
prompt = PromptTemplate.from_template("Generate tests in Python (compatible with pytest) that produce 100% code coverage. Output only Python code and nothing else before or after. \n ```py\n{code}\n```")

for function in itertools.chain(glob.glob("functions/*.py")):
    # Get code and create prompt
    print(function)
    with open(function) as f:
        code = f.read()
    code_prompt = prompt.format(code=code)
    
    # Generate tests and clean up output
    output = llm.predict(code_prompt)
    output = output.replace("```python", "").replace("```py", "").replace("```", "").strip()

    # Write out final code
    with open(function.replace("functions/", "tests/"), "w") as f:
        f.write(output)