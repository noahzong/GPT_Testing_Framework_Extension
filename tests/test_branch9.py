from functions.branch9 import branch9
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (2, 1, 3),
    (1, 2, -1),
    (2, 2, 1),
    (4, 2, 8),
    (3, 3, 27),
    (11, 1, 22),
    (2, -2, 12),
    (8, 8, 64),
    (9, 9, 405)
])
def test_branch9(a, b, expected):
    assert branch9(a, b) == expected