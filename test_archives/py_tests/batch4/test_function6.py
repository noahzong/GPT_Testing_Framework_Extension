from functions.function6 import function6
import pytest

def test_function6_1():
    assert function6("a", 2, [1,2,3], 4.2, True) == 424.0

def test_function6_2():
    assert function6("b", 3, [4,5], 10.2, False) == 3060.0