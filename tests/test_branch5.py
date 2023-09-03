from functions.branch5 import branch5
import pytest

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (1, 2, -1),
        (2, 1, 3),
        (2, 2, 4),
        (3, 2, 9),
        (-10, 10, 10)
    ]
)
def test_branch5(num1, num2, expected):
    assert branch5(num1, num2) == expected