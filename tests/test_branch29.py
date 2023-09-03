from functions.branch29 import branch29
import pytest

def test_branch29_x_gt_0_y_gt_0():
    assert branch29(2, 3) == 5

def test_branch29_x_gt_0_y_le_0():
    assert branch29(2, -3) == 5

def test_branch29_x_le_0_y_gt_0():
    assert branch29(-2, 3) == 5

def test_branch29_x_le_0_y_le_0():
    assert branch29(-2, -3) == 6