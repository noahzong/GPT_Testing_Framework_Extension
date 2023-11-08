from functions.function7 import function7
import pytest

def test_function7_1():
    assert function7(1, 2.0, True, 'test', [1, 2, 3], {'a':1, 'b':2}) == 13

def test_function7_2():
    assert function7(2, 3.3, False, '', [], {}) == 5.3