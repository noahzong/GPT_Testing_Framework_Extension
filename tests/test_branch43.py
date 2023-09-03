from functions.branch43 import branch43
import pytest

def test_branch43_1():
    assert branch43(2, 1, 3) == 5

def test_branch43_2():
    assert branch43(1, 2, 3) == 5

def test_branch43_3():
    assert branch43(3, 1, 2) == 5

def test_branch43_4():
    assert branch43(1, 3, 2) == 5

def test_branch43_5():
    assert branch43(2, 3, 1) == 5

def test_branch43_6():
    assert branch43(3, 2, 1) == 5