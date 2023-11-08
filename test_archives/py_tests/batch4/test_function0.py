from functions.function0 import function0
import pytest

def test_function0_1():
    assert function0('A', 'B', 5, 10.5, True) == 'AB510.5'

def test_function0_2():
    assert function0('C', 'D', 3, 7.2, False) == 'CD37.2'