from functions.branch45 import branch45
import pytest

@pytest.mark.parametrize('x,y,expected', [
    (1,2,2),
    (2,1,4),
    (5,5,25)
])
def test_branch45(x, y, expected):
    assert branch45(x,y) == expected