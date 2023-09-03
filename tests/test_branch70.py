from functions.branch70 import branch70
import pytest

def test_branch70_equal_greater_sum():
    assert branch70(2, 2, 1) == 4

def test_branch70_equal_equal_product():
    assert branch70(2, 2, 2) == 4

def test_branch70_equal_less_num3():
    assert branch70(2, 2, 3) == 3

def test_branch70_not_equal_greater_difference():
    assert branch70(3, 2, 1) == 1

def test_branch70_not_equal_less_sum():
    assert branch70(2, 3, 1) == 5

def test_branch70_not_equal_not_less_num3():
    assert branch70(3, 2, 2) == 3