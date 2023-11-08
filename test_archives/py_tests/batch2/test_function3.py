from functions.function3 import function3
import pytest

def test_function3_1():
    assert function3("yes", 2, 3.5) == 17.0

def test_function3_2():
    assert function3("no", 4, 6.2) == 19.8