from functions.branch81 import branch81
import pytest

def test_branch81_a_positive_b_equal_c():
    assert branch81(1, 2, 2) == 3

def test_branch81_a_positive_b_not_equal_c():
    assert branch81(1, 2, 3) == -1

def test_branch81_a_negative_c_positive():
    assert branch81(-1, 2, 3) == 5

def test_branch81_a_negative_c_negative():
    assert branch81(-1, 2, -3) == -1