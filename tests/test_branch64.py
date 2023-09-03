from functions.branch64 import branch64
import pytest

@pytest.mark.parametrize('x,y,z,expected',[(11,12,0,0),(11,11,-1,1),(11,11,1,2),(9,12,0,3),(9,11,-1,4),(9,11,1,5),(10,12,0,6),(10,11,-1,7),(10,11,1,8),(11,9,0,9),(11,10,-1,10),(11,10,1,11)])
def test_branch64(x,y,z,expected):
    assert branch64(x,y,z) == expected