from functions.branch19 import branch19
import pytest

def test_branch19_x_eq_0_y_eq_0():
    assert branch19(0, 0, 0) == True

def test_branch19_x_eq_0_y_neq_0():
    assert branch19(0, 1, 0) == False

def test_branch19_x_neq_0_z_eq_0():
    assert branch19(1, 0, 0) == False

def test_branch19_x_gt_0():
    assert branch19(1, 1, 1) == 1

def test_branch19_x_lt_0():
    assert branch19(-1, 1, 1) == -1