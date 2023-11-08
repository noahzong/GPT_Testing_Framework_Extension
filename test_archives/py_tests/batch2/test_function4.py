from functions.function4 import function4
import pytest

@pytest.mark.parametrize("num1, num2, num3, string1, list1, expected", [
  (1, 2, 3, 'abc', [1, 2, 3], 15),
  (2, 4, 6, 'def', [4, 5, 6], 30)
])
def test_function4(num1, num2, num3, string1, list1, expected):
  assert function4(num1, num2, num3, string1, list1) == expected