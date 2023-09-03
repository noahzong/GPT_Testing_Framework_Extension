from functions.branch91 import branch91
import pytest

def test_branch91_1():
    assert branch91(0,0) == 0

def test_branch91_2():
    assert branch91(0,1) == 1

def test_branch91_3():
    assert branch91(1,0) == 2

def test_branch91_4():
    assert branch91(1,1) == 3

def test_branch91_5():
    assert branch91(2,0) == 4

def test_branch91_6():
    assert branch91(2,1) == 5

def test_branch91_7():
    assert branch91(3,0) == 6

def test_branch91_8():
    assert branch91(3,1) == 7

def test_branch91_9():
    assert branch91(4,0) == 8

def test_branch91_10():
    assert branch91(4,1) == 9

def test_branch91_11():
    assert branch91(5,1) == -1