from functions.function3 import function3
import pytest

def test_function3_1():
    assert function3(1, 2, 'name') == 21.5

def test_function3_2():
    assert function3(2, 4, 'age') == 34.75