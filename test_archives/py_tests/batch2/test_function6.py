from functions.function6 import function6
import pytest

def test_function6_1():
    assert function6('John', 20, True, 3) == 28.35

def test_function6_2():
    assert function6('Jane', 25, False, 4) == 42.0