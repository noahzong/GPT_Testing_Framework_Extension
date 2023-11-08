from functions.function9 import function9
import pytest
def test_function9_1():
    assert function9("abc", 3, True) == "abc3"

def test_function9_2():
    assert function9("def", 5, False) == ""