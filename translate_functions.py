from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from tqdm import tqdm
import os

# Initialize the langchain model or API
llm = OpenAI(max_tokens=2048)

# Define a template for the translation prompt
prompt_template = "Translate the following Python class to valid C++ code. Remember to include appropriate header files, and using namespace std. Make all class members public.\n\n{}"

# Directory containing the Python functions
input_dir = 'functions'

# Directory to save the translated C++ functions
output_dir = 'translated_cpp'
os.makedirs(output_dir, exist_ok=True)

# Get a list of all Python files in the 'functions' directory
python_files = [f for f in os.listdir(input_dir) if f.endswith(".py")]

# Loop through each Python file
for filename in tqdm(python_files):
    with open(os.path.join(input_dir, filename), 'r') as py_file:
        python_code = py_file.read()
        
        # Create the prompt for translation
        prompt = prompt_template.format(python_code)
        
        # Get the translated C++ code using langchain (or your method of choice)
        cpp_code = llm.predict(prompt)
        
        # Clean up the translated code if needed (similar to your cleanup for Python code)
        cpp_code = cpp_code.replace("```cpp", "").replace("```c++", "").replace("```", "").strip()
        
        # Save the translated C++ code to a file
        output_filename = os.path.splitext(filename)[0] + ".cpp"
        with open(os.path.join(output_dir, output_filename), 'w') as cpp_file:
            cpp_file.write(cpp_code)

print("Translation completed!")
