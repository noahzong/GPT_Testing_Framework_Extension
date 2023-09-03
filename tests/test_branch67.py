from functions.branch67 import branch67
import pytest
 
def test_branch67_x_gt_10():
    x = 11
    y = 5
    z = 6
    assert branch67(x, y, z) == 22
 
def test_branch67_x_eq_10():
    x = 10
    y = 5
    z = 6
    assert branch67(x, y, z) == 300
 
def test_branch67_x_lt_10_y_gt_0_and_lt_10():
    x = 9
    y = 5
    z = 6
    assert branch67(x, y, z) == 45
 
def test_branch67_x_lt_10_y_lt_0_or_gt_10():
    x = 9
    y = -5
    z = 6
    assert branch67(x, y, z) == 9