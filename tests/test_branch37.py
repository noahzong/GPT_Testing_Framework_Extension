from functions.branch37 import branch37
import pytest

@pytest.mark.parametrize("x, y, z, expected", [
    (1, 2, 3, 6),
    (1, 2, -3, 3),
    (1, -2, 3, 4),
    (1, -2, -3, 1),
    (-1, 2, 3, 5),
    (-1, 2, -3, 2),
    (-1, -2, 3, 3),
    (-1, -2, -3, None)
])
def test_branch37(x, y, z, expected):
    assert branch37(x, y, z) == expected