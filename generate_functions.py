from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from tqdm import tqdm

llm = OpenAI(max_tokens=2048)
prompt = PromptTemplate.from_template("Generate a sample Python function with a lot of branches. If you want any user input, take it in as parameters. Be sure to return final values. Include just the function, and name it {branch}.")

for i in tqdm(range(100)):
    code_prompt = prompt.format(branch=f"branch{i}")
    output = llm.predict(code_prompt)
    output = output.replace("```python", "").replace("```py", "").replace("```", "").strip()
    with open(f"functions/branch{i}.py", "w") as f:
        f.write(output)