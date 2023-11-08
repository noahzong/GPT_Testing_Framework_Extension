from functions.function0 import function0
import pytest

def test_function0_1():
    assert function0(1, 2, 'a', 'b', 3) == 9

def test_function0_2():
    assert function0(2, 4, 'c', 'd', 5) == 30