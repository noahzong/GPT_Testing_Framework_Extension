from functions.branch22 import branch22
import pytest

def test_branch22_1():
    assert branch22(0, 0, 0) == 0

def test_branch22_2():
    assert branch22(0, 0, 1) == 1

def test_branch22_3():
    assert branch22(0, 1, 0) == 2

def test_branch22_4():
    assert branch22(0, 1, 1) == 3

def test_branch22_5():
    assert branch22(1, 0, 0) == 4

def test_branch22_6():
    assert branch22(1, 0, 1) == 5

def test_branch22_7():
    assert branch22(1, 1, 0) == 6

def test_branch22_8():
    assert branch22(1, 1, 1) == 7