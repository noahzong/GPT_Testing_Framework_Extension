from functions.branch84 import branch84
import pytest

def test_branch84_A_greater():
    assert branch84(3, 2, "A") == 5

def test_branch84_A_less():
    assert branch84(2, 3, "A") == 6

def test_branch84_A_equal():
    assert branch84(2, 2, "A") == 4

def test_branch84_B_greater():
    assert branch84(3, 2, "B") == 1

def test_branch84_B_less():
    assert branch84(2, 3, "B") == 1

def test_branch84_B_equal():
    assert branch84(2, 2, "B") == 1

def test_branch84_neither_greater():
    assert branch84(2, 3, "C") == 4

def test_branch84_neither_less():
    assert branch84(3, 2, "C") == 5

def test_branch84_neither_equal():
    assert branch84(2, 2, "C") == 8