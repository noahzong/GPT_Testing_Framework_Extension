from functions.branch44 import branch44
import pytest

def test_branch44_1():
    assert branch44(0, 0, 1, 2) == 0

def test_branch44_2():
    assert branch44(1, 0, 1, 2) == 3

def test_branch44_3():
    assert branch44(0, 1, 1, 2) == 2

def test_branch44_4():
    assert branch44(1, 1, 1, 2) == 0.5

def test_branch44_5():
    assert branch44(2, 2, 1, 2) == -1