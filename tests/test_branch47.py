from functions.branch47 import branch47
import pytest

def test_branch47_x_0():
  assert branch47(0, 5, 3) == 8

def test_branch47_x_positive_y_0():
  assert branch47(5, 0, 3) == 2

def test_branch47_x_negative_y_negative():
  assert branch47(-2, -3, 4) == -8

def test_branch47_x_positive_y_positive_z_0():
  assert branch47(2, 3, 0) == 0.666

def test_branch47_x_positive_y_positive_z_positive():
  assert branch47(2, 3, 4) == 9

def test_branch47_invalid_input():
  assert branch47(2, -3, 4) == "Invalid input"