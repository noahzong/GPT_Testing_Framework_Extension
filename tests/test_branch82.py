from functions.branch82 import branch82
import pytest

def test_branch82_neg_x():
    assert branch82(-2, 3) == 1

def test_branch82_zero_x():
    assert branch82(0, 4) == 0

def test_branch82_pos_x_pos_y():
    assert branch82(2, 3) == 5

def test_branch82_pos_x_neg_y():
    assert branch82(2, -3) == -1