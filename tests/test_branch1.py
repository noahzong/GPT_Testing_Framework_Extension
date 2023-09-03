from functions.branch1 import branch1
import pytest

@pytest.mark.parametrize('param1, param2, param3, expected_result', 
[(11, 15, 40, 155),
 (11, 20, 40, 51),
 (8, 15, 40, 48),
 (8, 15, 5, 13),
 (8, 15, 0, 8)])
def test_branch1(param1, param2, param3, expected_result):
    result = branch1(param1, param2, param3)
    assert result == expected_result