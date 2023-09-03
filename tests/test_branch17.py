from functions.branch17 import branch17
import pytest

@pytest.mark.parametrize("x, y, expected", [(0, 0, 0), (0, 1, 1), (1, 0, 1), (4, 5, 20)])
def test_branch17(x, y, expected):
    assert branch17(x, y) == expected