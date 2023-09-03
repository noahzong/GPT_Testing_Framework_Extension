from functions.branch80 import branch80
import pytest

@pytest.mark.parametrize('num1, num2, num3, expected', 
[
    (5, 4, 1, 1),
    (4, 4, 1, 0),
    (3, 4, 1, -1),
    (5, 4, 2, 2),
    (4, 4, 2, 0),
    (3, 4, 2, -2),
    (5, 4, 3, 3),
    (4, 4, 3, 0),
    (3, 4, 3, -3)
])
def test_branch80(num1, num2, num3, expected):
    assert branch80(num1, num2, num3) == expected