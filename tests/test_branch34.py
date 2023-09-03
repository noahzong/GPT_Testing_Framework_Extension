from functions.branch34 import branch34
import pytest

def test_branch34_positive():
    assert branch34(2, 2) == 4

def test_branch34_opposite_negative():
    assert branch34(-1, -2) == -3

def test_branch34_one_zero():
    assert branch34(0, 4) == 0

def test_branch34_different_signs():
    assert branch34(-3, 2) == -1