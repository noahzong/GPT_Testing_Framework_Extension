from functions.branch54 import branch54
import pytest

@pytest.mark.parametrize("num1, num2, num3, expected", 
                        [(1, 2, 3, 3),
                         (3, 2, 1, 3),
                         (2, 3, 1, 3),
                         (4, 3, 2, 4)])
def test_branch54(num1, num2, num3, expected):
    assert branch54(num1, num2, num3) == expected