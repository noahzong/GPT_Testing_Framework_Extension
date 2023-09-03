# Test Case Generation Benchmark
*Made for Fall 2023 CS 8395-08*

This benchmark is evaluating the performance of different LLM's test case generation for code coverage. 100 Python functions are contained in the `functions/` folder, and the LLM is asked to generate test cases for the function such that it will have 100% code coverage. Many of the functions were generated using `text-davinci-003` (see `generate_functions.py`). This is novel because it's explicitly trying to get higher code coverage, which requires the LLM to understand the branches in the code. This can be a difficult problem if there are multiple stages of branching -- for example, if one set of branches creates an intermediate value, and then after that, another set of branches manipulates that values and returns it, it might be hard for the LLM to understand what sort of values could be used to cover the second set of branches.

## Running the Benchmark
- Delete `tests/`
- Install packages: `pip3 install -r requirements.txt`
- Run `python3 generate_tests.py` to generate tests using the model. Feel free to swap out the LLM used on line 9.
- Evaluate coverage by running `bash check_coverage.bash`. This will print out the coverage for each function, as well as the average coverage for all functions. As an added bonus, it will also show what percentage of the tests were valid.