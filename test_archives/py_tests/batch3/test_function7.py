from functions.function7 import function7
import pytest

def test_function7_1(): 
    assert function7("Hello", 2, [3, 4, 5]) == 22
    
def test_function7_2(): 
    assert function7("World", 3, [1,2,3,4,5]) == 30.0