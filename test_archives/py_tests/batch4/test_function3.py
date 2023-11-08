from functions.function3 import function3
import pytest

def test_function3_1():
    assert function3('2', '3', 4.5, 3) == 5.0

def test_function3_2():
    assert function3('4', '6', 2.2, 8) == 6.8