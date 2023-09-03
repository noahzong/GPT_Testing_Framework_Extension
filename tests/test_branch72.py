from functions.branch72 import branch72
import pytest

def test_branch72_1_2(): 
    assert branch72(1, 2) == 'A'

def test_branch72_2_1(): 
    assert branch72(2, 1) == 'C'

def test_branch72_1_3(): 
    assert branch72(1, 3) == 'B'

def test_branch72_2_2(): 
    assert branch72(2, 2) == 'D'

def test_branch72_3_1(): 
    assert branch72(3, 1) == 'E'

def test_branch72_3_2(): 
    assert branch72(3, 2) == 'F'