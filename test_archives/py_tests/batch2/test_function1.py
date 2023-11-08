from functions.function1 import function1
import pytest

def test_function1_1():
    assert function1("string", 2, True) == "string2"

def test_function1_2():
    assert function1("string", 2, False) == "string4"