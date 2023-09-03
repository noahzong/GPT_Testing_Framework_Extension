from functions.branch68 import branch68
import pytest

def test_branch68_1():
    assert branch68(1,2,3) == 14

def test_branch68_2():
    assert branch68(1,-2,3) == -4

def test_branch68_3():
    assert branch68(-1,2,-3) == -4

def test_branch68_4():
    assert branch68(-1,-2,-3) == 14

def test_branch68_5():
    assert branch68(0,0,0) == 0