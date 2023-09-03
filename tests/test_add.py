from functions.add import add
import pytest

def test_add_positive_numbers():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -3) == -4

def test_add_positive_and_negative_numbers():
    assert add(-1, 2) == 1

def test_add_zero():
    assert add(1, 0) == 1
    assert add(0, 0) == 0