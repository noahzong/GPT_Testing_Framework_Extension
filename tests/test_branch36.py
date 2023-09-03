from functions.branch36 import branch36
import pytest

def test_branch36_equal():
    assert branch36(1, 1) == 1

def test_branch36_greater():
    assert branch36(2, 1) == 2

def test_branch36_lesser():
    assert branch36(1, 2) == 3

def test_branch36_zero():
    assert branch36(0, 1) == 4

def test_branch36_both_zero():
    assert branch36(0, 0) == 5

def test_branch36_negative():
    assert branch36(-1, 1) == 6

def test_branch36_both_one():
    assert branch36(1, 1) == 7

def test_branch36_both_div_3():
    assert branch36(6, 9) == 8

def test_branch36_div_5():
    assert branch36(5, 6) == 9

def test_branch36_div_7():
    assert branch36(7, 14) == 10

def test_branch36_sum_7():
    assert branch36(3, 4) == 11

def test_branch36_default():
    assert branch36(2, 3) == 0