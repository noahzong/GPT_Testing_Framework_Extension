from functions.function9 import function9
import pytest

def test_function9_1(): 
    assert function9('abc', 'def', 1, 2.3) == 9.3

def test_function9_2(): 
    assert function9('xyz', 'uvw', 5, 7.8) == 18.8