from functions.branch7 import branch7
import pytest

@pytest.mark.parametrize("x, y, z, expected", [
    (1, 2, 3, 7),
    (-1, -2, -3, -4),
    (0, 0, 0, 0),
    (1, 0, 3, 4),
    (-1, 2, 0, 1),
    (1, -2, 3, 4),
    (0, -2, 3, 1),
    (1, 2, -3, 7),
    (-1, 0, 3, 2)
])
def test_branch7(x, y, z, expected):
    assert branch7(x, y, z) == expected