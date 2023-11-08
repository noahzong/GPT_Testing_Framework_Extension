from functions.function4 import function4
import pytest

def test_function4_1():
    assert function4(6, "Hello", [2, 5, 8]) == 54.0

def test_function4_2():
    assert function4(9, "World", [1, 3, 4]) == 66.0