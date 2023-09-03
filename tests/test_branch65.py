from functions.branch65 import branch65
import pytest

def test_branch65_zero_zero():
    assert branch65(0, 0) == 0

def test_branch65_zero_positive():
    assert branch65(0, 5) == 5

def test_branch65_positive_zero():
    assert branch65(10, 0) == 10

def test_branch65_positive_positive():
    assert branch65(10, 5) == 50

def test_branch65_negative_zero():
    assert branch65(-10, 0) == 10

def test_branch65_negative_positive():
    assert branch65(-10, 5) == -5

def test_branch65_zero_negative():
    assert branch65(0, -5) == -5

def test_branch65_positive_negative():
    assert branch65(10, -5) == 5

def test_branch65_negative_negative():
    assert branch65(-10, -5) == 2