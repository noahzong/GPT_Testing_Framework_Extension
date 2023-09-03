from functions.branch59 import branch59
import pytest

def test_branch59_1():
    assert branch59(0, 0) == 0

def test_branch59_2():
    assert branch59(0, 1) == 1

def test_branch59_3():
    assert branch59(-1, 0) == -1

def test_branch59_4():
    assert branch59(-1, 1) == 0

def test_branch59_5():
    assert branch59(-1, -1) == -2

def test_branch59_6():
    assert branch59(1, 0) == 0

def test_branch59_7():
    assert branch59(1, 1) == 0

def test_branch59_8():
    assert branch59(1, -1) == 2