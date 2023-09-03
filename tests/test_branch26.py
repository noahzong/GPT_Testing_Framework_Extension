from functions.branch26 import branch26
import pytest

def test_branch26_first_branch():
    assert branch26(3, 2, 1) == 6
    
def test_branch26_second_branch():
    assert branch26(3, 1, 2) == 6
    
def test_branch26_third_branch():
    assert branch26(2, 3, 1) == 2
    
def test_branch26_fourth_branch():
    assert branch26(2, 2, 2) == 8
    
def test_branch26_fifth_branch():
    assert branch26(1, 2, 3) == 0