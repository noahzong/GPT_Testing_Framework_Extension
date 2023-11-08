from functions.function2 import function2
import pytest

def test_function2(): 
  assert function2(1, 2, "abc", [1, 2, 3], True) == 12 
  assert function2(2, 4, "def", [4, 5, 6], False) == 7 
  assert function2(3, 6, "ghi", [7, 8, 9], True) == 18 
  assert function2(4, 8, "jkl", [10, 11, 12], False) == 5