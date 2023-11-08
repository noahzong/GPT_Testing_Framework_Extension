from functions.function9 import function9
import pytest

@pytest.mark.parametrize("string_input, int_input, list_input, expected_result", 
[
    ("Test", 1, [1, 2, 3], 0),
    ("Test2", 2, [3, 4, 5], 0)
])
def test_process_data(string_input, int_input, list_input, expected_result):
    instance = function9(string_input, int_input, list_input)
    assert instance.process_data() == expected_result