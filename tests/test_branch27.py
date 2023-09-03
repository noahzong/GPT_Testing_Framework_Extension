from functions.branch27 import branch27
import pytest

@pytest.mark.parametrize("input1,input2,expected", [
    (0, 0, 0),
    (0, 1, 1),
    (0, 2, 2),
    (1, 0, 3),
    (1, 1, 4),
    (1, 2, 5),
    (2, 0, 6),
    (2, 1, 7),
    (2, 2, 8)
])
def test_branch27(input1, input2, expected):
    assert branch27(input1, input2) == expected