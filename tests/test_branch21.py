from functions.branch21 import branch21
import pytest

@pytest.mark.parametrize("num1, num2, expected", [
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 2),
    (3, 6, 9),
    (-1, -2, 2),
    (7, -3, 10),
    (-7, 3, -10),
    (4, 4, 16)
])
def test_branch21(num1, num2, expected):
    assert branch21(num1, num2) == expected