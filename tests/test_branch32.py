from functions.branch32 import branch32
import pytest

def test_branch32_sum_zero():
    assert branch32(0, 0) == 0

def test_branch32_x_zero():
    assert branch32(0, 1) == 1

def test_branch32_y_zero():
    assert branch32(1, 0) == 1

def test_branch32_both_non_zero():
    assert branch32(2, 3) == 11