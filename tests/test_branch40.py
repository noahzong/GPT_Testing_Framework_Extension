from functions.branch40 import branch40
import pytest

def test_branch40_1():
    assert branch40(1, 1, 1, 1) == 4

def test_branch40_2():
    assert branch40(1, 1, 0, 1) == 0

def test_branch40_3():
    assert branch40(1, 0, 1, 1) == 2

def test_branch40_4():
    assert branch40(0, 1, 1, 1) == -1

def test_branch40_5():
    assert branch40(1, 1, 1, 0) == 3

def test_branch40_6():
    assert branch40(1, 1, 0, 0) == 0

def test_branch40_7():
    assert branch40(1, 0, 1, 0) == 1

def test_branch40_8():
    assert branch40(0, 1, 1, 0) == -1

def test_branch40_9():
    assert branch40(0, 0, 0, 0) == 0