from functions.function0 import function0
import pytest

@pytest.mark.parametrize('int_input, float_input, list_input, expected', [
    (1, 2.5, [2, 3], 15),
    (2, 3.5, [1, 2], 14),
    (3, 4.5, [3, 4], 162)
])
def test_multiply_result(int_input, float_input, list_input, expected):
    f0 = function0(int_input, float_input, 'test', list_input)
    result = f0.multiply_result()
    assert result == expected