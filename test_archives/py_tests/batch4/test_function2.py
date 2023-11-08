from functions.function2 import function2
import pytest

def test_function2_1():
    assert function2("test", 1, 2, [1, 2, 3]) == 4.0

def test_function2_2():
    assert function2("test", 2, 4, [1, 2, 3, 4, 5]) == 4.8