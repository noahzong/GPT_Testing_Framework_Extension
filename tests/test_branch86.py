from functions.branch86 import branch86
import pytest

def test_branch86_x_eq_0_y_eq_0():
    assert branch86(0, 0) == 0

def test_branch86_x_eq_0_y_not_eq_0():
    assert branch86(0, 1) == 1

def test_branch86_x_not_eq_0_y_eq_0():
    assert branch86(1, 0) == 1

def test_branch86_x_not_eq_0_y_not_eq_0():
    assert branch86(1, 1) == 1