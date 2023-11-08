from functions.function0 import function0
import pytest
def test_function0_1():
  assert function0(1, 2.3, 'hello', True) == 3.3

def test_function0_2():
  assert function0(2, 4.6, 'world', False) == 0

def test_function0_3():
  assert function0(3, 6.9, 'hello', False) == 6.9

def test_function0_4():
  assert function0(4, 9.2, 'world', True) == 4