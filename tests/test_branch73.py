from functions.branch73 import branch73
import pytest

def test_branch73_1():
    assert branch73(7, 8, 9) == 30

def test_branch73_2():
    assert branch73(8, 7, 9) == 24

def test_branch73_3():
    assert branch73(7, 7, 9) == 33

def test_branch73_4():
    assert branch73(7, 8, 8) == 27