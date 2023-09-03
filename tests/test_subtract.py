from functions.subtract import subtract
import pytest

def test_subtract_positive():
    assert subtract(3, 2) == 1

def test_subtract_negative():
    assert subtract(2, 3) == -1

def test_subtract_zero():
    assert subtract(1, 1) == 0