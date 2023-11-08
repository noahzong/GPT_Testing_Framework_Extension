from functions.function7 import function7
import pytest
def test_function7_1():
    assert function7("Hello", 1, 2, True) == "Hello 3"

def test_function7_2():
    assert function7("World", 3, 4, False) == "World 12"