from functions.function7 import function7
import pytest 

def test_function7_1(): 
    assert function7(1, "abc", 2.5, ["a", "b"]) == 4.5

def test_function7_2(): 
    assert function7(3, "xyz", 3.5, ["x", "y"]) == 12.5