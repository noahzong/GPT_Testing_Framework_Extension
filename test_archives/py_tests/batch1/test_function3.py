from functions.function3 import function3
import pytest
def test_function3_1():
    assert function3('a', 1, {'x': 2, 'y': 3}, True) == 'a15True'

def test_function3_2():
    assert function3('b', 2, {'x': 4, 'y': 5}, False) == 'b29False'