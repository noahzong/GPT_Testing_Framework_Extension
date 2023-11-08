from functions.function1 import function1
import pytest
def test_function1_1(): 
    assert function1("abc", [1,2,3]) == 90

def test_function1_2(): 
    assert function1("xyz", [4,5,6], 5) == 45