from functions.function2 import function2
import pytest

def test_function2_1():
    assert function2("ABC", 1, 2.3) == 6

def test_function2_2():
    assert function2("ABCD", 2, 3.5) == 28