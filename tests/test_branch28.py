from functions.branch28 import branch28
import pytest

@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),
    (-1, -2, 2),
    (1, -2, -1),
    (-1, 2, 1),
    (0, 0, 0),
    (3, -1, 2)
])
def test_branch28(x, y, expected):
    assert branch28(x, y) == expected