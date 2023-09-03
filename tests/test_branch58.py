from functions.branch58 import branch58
import pytest

@pytest.mark.parametrize("num1, num2, expected", [
  (5, 10, 15),
  (10, 5, 0),
  (2, 4, 8),
  (-2, 4, -0.5),
  (2, -4, -2),
  (4, 0, 4),
  (1, -2, -3),
  (2, 0, 2)
])
def test_branch58(num1, num2, expected):
  assert branch58(num1, num2) == expected