from functions.branch83 import branch83
import pytest

def test_branch83_positive_positive():
    assert branch83(1, 2) == 3
    
def test_branch83_positive_negative():
    assert branch83(1, -2) == -1

def test_branch83_positive_zero():
    assert branch83(1, 0) == 1

def test_branch83_negative_positive():
    assert branch83(-1, 2) == 1

def test_branch83_negative_negative():
    assert branch83(-1, -2) == 3

def test_branch83_negative_zero():
    assert branch83(-1, 0) == -1

def test_branch83_zero_positive():
    assert branch83(0, 2) == 2

def test_branch83_zero_negative():
    assert branch83(0, -2) == -2

def test_branch83_zero_zero():
    assert branch83(0, 0) == 0