from functions.function5 import function5
import pytest

def test_function5_1():
    assert function5(1, 'abc', 2.5, [1,2,3]) == 9.5

def test_function5_2():
    assert function5(3, 'xy', 4.8, [4,5,6,7]) == 13.8