from functions.branch99 import branch99
import pytest

@pytest.mark.parametrize("x, y, expected", [
    (0, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (2, 3, 6)
])
def test_branch99(x, y, expected):
    assert branch99(x, y) == expected