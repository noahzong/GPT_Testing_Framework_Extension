from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from tqdm import tqdm

llm = OpenAI(max_tokens=2048)
prompt = PromptTemplate.from_template("Generate a sample Python class with a lot of variables and data types. If you want any user input, take it in as parameters. The class's methods should return one singular final value. Include just the class, and name it {function}.")

for i in tqdm(range(10)):
    code_prompt = prompt.format(function=f"function{i}")
    output = llm.predict(code_prompt)
    output = output.replace("```python", "").replace("```py", "").replace("```", "").strip()
    with open(f"functions/function{i}.py", "w") as f:
        f.write(output)