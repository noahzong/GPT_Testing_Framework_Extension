from functions.function6 import function6
import pytest

def test_function6_1():
    assert function6("John", 20, True, True) == "John is 20 years old. They like pizza. They are an active member."

def test_function6_2():
    assert function6("Mary", 18, False, False) == "Mary is 18 years old. They don't like pizza. They are not an active member."