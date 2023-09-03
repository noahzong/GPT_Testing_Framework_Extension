from functions.branch61 import branch61
import pytest
    
def test_branch61_0_0():
    assert branch61(0, 0) == 0

def test_branch61_x_y():
    assert branch61(1,1) == 2

def test_branch61_x_y_neg():
    assert branch61(-1, -1) == 2

def test_branch61_x_neg_y():
    assert branch61(1,-1) == -1

def test_branch61_x_neg_y_pos():
    assert branch61(-1, 1) == -1

def test_branch61_error():
    assert branch61(3, -2) == "Error"