from functions.function1 import function1
import pytest

def test_function1_1():
    assert function1('foo', 1, True) == 12

def test_function1_2():
    assert function1('bar', 2, False) == 3