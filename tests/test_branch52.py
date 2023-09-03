from functions.branch52 import branch52
import pytest

@pytest.mark.parametrize("a, b, c, result", [
    (2, 3, 4, 9), 
    (2, 3, -4, -2), 
    (2, -3, 4, -1), 
    (2, -3, -4, -1.5), 
    (-2, 3, 4, -3), 
    (-2, 3, -4, 1), 
    (-2, -3, 4, 4), 
    (-2, -3, -4, -5)
])
def test_branch52(a, b, c, result):
    assert branch52(a, b, c) == result