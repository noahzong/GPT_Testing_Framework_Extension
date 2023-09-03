from functions.branch94 import branch94
import pytest

def test_branch94():
    assert branch94(1,2,3) == 3
    assert branch94(2,1,3) == 3
    assert branch94(3,2,1) == 3
    assert branch94(1,3,2) == 3
    assert branch94(2,3,1) == 3
    assert branch94(3,1,2) == 3
    assert branch94(1,1,3) == 2
    assert branch94(1,3,1) == 2
    assert branch94(3,1,1) == 2
    assert branch94(1,2,2) == 3
    assert branch94(2,1,2) == 3
    assert branch94(2,2,1) == 3
    assert branch94(1,1,1) == 3