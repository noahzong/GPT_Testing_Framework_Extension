from functions.function6 import function6
import pytest

def test_function6_1():  
  assert function6(1, 'hello world', ['foo', 'bar']) == 6

def test_function6_2():  
  assert function6(2, 'how are you', ['baz', 'qux']) == 8