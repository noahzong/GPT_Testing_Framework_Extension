from functions.function1 import function1
import pytest

def test_function1_1(): 
    assert function1('abc', 3, 1.5, [2, 4, 6]) == 'abcabcabc27.0'

def test_function1_2(): 
    assert function1('xyz', 4, 2.5, [3, 6, 9]) == 'xyzxyzxyzxyz112.5'