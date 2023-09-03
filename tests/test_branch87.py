from functions.branch87 import branch87
import pytest

def test_branch87_1():
    assert branch87(2, 3) == 5

def test_branch87_2():
    assert branch87(-2, -3) == 5

def test_branch87_3():
    assert branch87(0, 0) == 0

def test_branch87_4():
    assert branch87(2, -3) == -1

def test_branch87_5():
    assert branch87(-2, 3) == 1

def test_branch87_6():
    assert branch87(-2, 0) == -2