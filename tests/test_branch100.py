from functions.branch100 import branch100
import pytest

@pytest.mark.parametrize("num1, num2, num3, expected_result", [
    (0, 0, 0, 0),
    (0, 0, 10, 10),
    (0, 10, 0, 10),
    (10, 0, 0, 10),
    (0, 10, 10, 20),
    (10, 0, 10, 20),
    (10, 10, 0, 20),
    (10, 10, 10, 30)
])
def test_branch100(num1, num2, num3, expected_result):
    """Test the branch100 function"""
    result = branch100(num1, num2, num3)
    assert result == expected_result