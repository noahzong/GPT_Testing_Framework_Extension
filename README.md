# Test Case Generation Benchmark
This framework generates python functions and test cases, then translates them to C++ to help test gpt's code translation capabilities.

## Running the Benchmark
1. Ensure that functions, tests, translated_cpp, and translated_tests_cpp exist, but are empty

2. Generate python functions - run generate_functions.py. The prompt variable can be changed to customize the generation prompt

3.Generate python tests - run generate_tests.py --model openai-latest. In the config file, the prompt item can be changed to customize the generation prompt

4.Run python tests bash ./check_coverage.bash
Adjust python tests to be correct manually. Note- the test generation is very bad at generating correct tests

5.Translate functions to C++ - run translate_functions.py. The prompt variable can be changed to customize the translation prompt

6. Translate tests to C++ - run translate_tests.py --model openai-latest. The translation_prompt item can be changed to customize the translation prompt

From there, the translated tests are now able to run using the Catch2 C++ testing framework.
