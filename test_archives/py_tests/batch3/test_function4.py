from functions.function4 import function4
import pytest

def test_function4_1():
    assert function4(1, 2, 3.0, 4.0, 'hi', 'there', True, True) == '14hitherTrue'

def test_function4_2():
    assert function4(3, 4, 2.0, 4.1, 'hello', 'world', False, True) == '7hello worldFalse'