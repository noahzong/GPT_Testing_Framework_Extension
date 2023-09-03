from functions.branch79 import branch79
import pytest

def test_branch79_positive_positive():
    assert branch79(2,3) == 6

def test_branch79_negative_negative():
    assert branch79(-2,-3) == -5

def test_branch79_zero_non_zero():
    assert branch79(3,0) == 0
    assert branch79(0,4) == 8

def test_branch79_non_zero_non_zero():
    assert branch79(2,3) == 6
    assert branch79(-2,3) == -1
    assert branch79(2,-3) == -1