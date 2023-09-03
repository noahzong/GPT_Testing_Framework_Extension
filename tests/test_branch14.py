from functions.branch14 import branch14
import pytest

def test_branch14_x_gt_0_y_gt_0_z_gt_0():
    x = 1
    y = 1
    z = 1
    assert branch14(x, y, z) == 1

def test_branch14_x_gt_0_y_gt_0_z_le_0():
    x = 1
    y = 1
    z = 0
    assert branch14(x, y, z) == 2

def test_branch14_x_gt_0_y_le_0_z_gt_0():
    x = 1
    y = 0
    z = 1
    assert branch14(x, y, z) == 3

def test_branch14_x_gt_0_y_le_0_z_le_0():
    x = 1
    y = 0
    z = 0
    assert branch14(x, y, z) == 4

def test_branch14_x_le_0_y_gt_0_z_gt_0():
    x = 0
    y = 1
    z = 1
    assert branch14(x, y, z) == 5

def test_branch14_x_le_0_y_gt_0_z_le_0():
    x = 0
    y = 1
    z = 0
    assert branch14(x, y, z) == 6

def test_branch14_x_le_0_y_le_0_z_gt_0():
    x = 0
    y = 0
    z = 1
    assert branch14(x, y, z) == 7

def test_branch14_x_le_0_y_le_0_z_le_0():
    x = 0
    y = 0
    z = 0
    assert branch14(x, y, z) == 8