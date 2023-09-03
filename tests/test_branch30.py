from functions.branch30 import branch30
import pytest

def test_branch30_x_lt_0_y_gt_10_z_eq_0():
    assert branch30(-1, 11, 0) == -1

def test_branch30_x_lt_0_y_gt_10_z_ne_0():
    assert branch30(-1, 11, 1) == 0

def test_branch30_x_lt_0_y_lt_10_z_gt_0():
    assert branch30(-1, 9, 1) == 1

def test_branch30_x_lt_0_y_lt_10_z_le_0():
    assert branch30(-1, 9, 0) == 2

def test_branch30_x_gt_0_y_gt_10_z_eq_0():
    assert branch30(1, 11, 0) == 3

def test_branch30_x_gt_0_y_gt_10_z_ne_0():
    assert branch30(1, 11, 1) == 4

def test_branch30_x_gt_0_y_lt_10_z_gt_0():
    assert branch30(1, 9, 1) == 5

def test_branch30_x_gt_0_y_lt_10_z_le_0():
    assert branch30(1, 9, 0) == 6

def test_branch30_x_eq_0():
    assert branch30(0, 0, 0) == 7