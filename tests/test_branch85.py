from functions.branch85 import branch85
import pytest

def test_branch85_x_0_y_0():
    assert branch85(0, 0) == 0

def test_branch85_x_0_y_positive():
    assert branch85(0, 1) == 1

def test_branch85_x_0_y_negative():
    assert branch85(0, -1) == -1

def test_branch85_x_positive_y_0():
    assert branch85(1, 0) == 2

def test_branch85_x_positive_y_positive():
    assert branch85(1, 1) == 3

def test_branch85_x_positive_y_negative():
    assert branch85(1, -1) == 4

def test_branch85_x_negative_y_0():
    assert branch85(-1, 0) == 5

def test_branch85_x_negative_y_positive():
    assert branch85(-1, 1) == 6

def test_branch85_x_negative_y_negative():
    assert branch85(-1, -1) == 7