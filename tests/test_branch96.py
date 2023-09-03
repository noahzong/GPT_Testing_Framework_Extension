from functions.branch96 import branch96
import pytest

@pytest.mark.parametrize('a,b,c,expected',
    [(0,1,2,4),
    (1,1,2,3),
    (2,1,2,1),
    (2,-1,2,-1),
    (2,1,0,1)])

def test_branch96(a,b,c,expected):
    assert branch96(a,b,c) == expected