from functions.function4 import function4
# Generate tests
import pytest

def test_function4_1():
    assert function4(1, 2, 3) == 'b'

def test_function4_2():
    assert function4(2, 4, 6) == 'b'