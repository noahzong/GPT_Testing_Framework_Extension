from functions.branch88 import branch88
import pytest

@pytest.mark.parametrize("a,b,c,expected", [
    (0, 0, 0, 0),
    (0, 0, 1, 1),
    (0, 1, 0, 2),
    (1, 0, 0, 3),
    (1, 0, 1, 4),
    (1, 1, 0, 5),
    (1, 1, 1, 6)
])
def test_branch88(a, b, c, expected):
    assert branch88(a, b, c) == expected