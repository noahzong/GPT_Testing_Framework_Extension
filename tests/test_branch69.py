from functions.branch69 import branch69
import pytest

def test_branch_69():
    assert branch69(0, 0, 0) == 0
    assert branch69(0, 0, 1) == 1
    assert branch69(0, 1, 0) == 2
    assert branch69(0, 1, 1) == 3
    assert branch69(1, 0, 0) == 4
    assert branch69(1, 0, 1) == 5
    assert branch69(1, 1, 0) == 6
    assert branch69(1, 1, 1) == 7
    assert branch69(2, 0, 0) == 8
    assert branch69(2, 0, 1) == 9
    assert branch69(2, 1, 0) == 10
    assert branch69(2, 1, 1) == 11