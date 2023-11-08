from functions.function9 import function9
import pytest

def test_function9_1():
    assert function9(1, 2.5, "foo", [1,2,3]) == 12.5

def test_function9_2():
    assert function9(4, 7.2, "bar", [3,4,5]) == 26.2