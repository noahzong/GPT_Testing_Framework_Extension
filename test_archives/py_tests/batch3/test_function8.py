from functions.function8 import function8
import pytest 

def test_function8_1(): 
    assert function8(1, "abcd", True, 3) == 4 

def test_function8_2(): 
    assert function8(2, "efgh", False, 0) == 4