from functions.multiply import multiply
import pytest

def test_multiply_with_integers():
    assert multiply(2, 3) == 6

def test_multiply_with_floats():
    assert multiply(2.0, 3.0) == 6.0

def test_multiply_with_negative_numbers():
    assert multiply(-2, 3) == -6

def test_multiply_with_zero():
    assert multiply(2, 0) == 0