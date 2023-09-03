from functions.branch55 import branch55
import pytest

def test_branch55_1():
    assert branch55(-5, 10) == 5

def test_branch55_2():
    assert branch55(-5, 0) == -5

def test_branch55_3():
    assert branch55(-5, -10) == -15

def test_branch55_4():
    assert branch55(0, 10) == 10

def test_branch55_5():
    assert branch55(0, 0) == 0

def test_branch55_6():
    assert branch55(0, -10) == -10

def test_branch55_7():
    assert branch55(5, 10) == -5

def test_branch55_8():
    assert branch55(5, 0) == 5

def test_branch55_9():
    assert branch55(5, -10) == 15