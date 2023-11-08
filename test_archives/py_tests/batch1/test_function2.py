from functions.function2 import function2
import pytest
def test_function2_1():
    assert function2('hello', 1, [2,3]) == 11

def test_function2_2():
    assert function2('world', 3, [4,5,6]) == 23