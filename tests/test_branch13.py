from functions.branch13 import branch13
import pytest

def test_branch13():
  assert branch13(0, 0) == 0
  assert branch13(1, 0) == 1
  assert branch13(0, 1) == 1
  assert branch13(1, 1) == 2
  assert branch13(-1, -1) == 3
  assert branch13(1, -1) == 4
  assert branch13(-1, 1) == 5
  assert branch13(3, -4) == 5
  assert branch13(-5, 6) == 5
  assert branch13(7, 8) == 2
  assert branch13(-9, 10) == 3
  assert branch13(0, -11) == 4
  assert branch13(-12, 0) == 1
  assert branch13(-13, -14) == 3