from functions.function9 import function9
import pytest

def test_function9_1():
    assert function9('total = ', 1, 2, 3, [1, 2, 3]) == 'total = 24'

def test_function9_2():
    assert function9('sum = ', 2, 4, 6, [3, 5, 7]) == 'sum = 51'