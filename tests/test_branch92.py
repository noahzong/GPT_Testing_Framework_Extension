from functions.branch92 import branch92
import pytest

def test_branch92_case1():
    assert branch92(2, 1, 1, 3, 4) == 7

def test_branch92_case2():
    assert branch92(1, 2, 1, 5, 6) == 12

def test_branch92_case3():
    assert branch92(2, 1, 3, 5, 6) == 21

def test_branch92_case4():
    assert branch92(1, 2, 3, 4, 5) == 20