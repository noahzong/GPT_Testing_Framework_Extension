from functions.function0 import function0
import pytest

def test_function0_1(): 
    assert function0(1, 2.3, "four", [5, 6]) == 9.3

def test_function0_2(): 
    assert function0(2, 4.6, "eight", [10, 12]) == 13.6