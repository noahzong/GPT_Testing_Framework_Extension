from functions.function5 import function5
import pytest

def test_function5_1():
    assert function5(1, 2, 3) == 6

def test_function5_2():
    assert function5(2, 4, 6) == 12