from functions.branch74 import branch74
import pytest

def test_branch74_scenario1():
    x = 5
    y = 4
    assert branch74(x, y) == 1

def test_branch74_scenario2():
    x = 17
    y = 6
    assert branch74(x, y) == 18

def test_branch74_scenario3():
    x = 4
    y = 6
    assert branch74(x, y) == 15

def test_branch74_scenario4():
    x = 16
    y = 11
    assert branch74(x, y) == 33

def test_branch74_scenario5():
    x = 8
    y = 9
    assert branch74(x, y) == 13

def test_branch74_scenario6():
    x = 9
    y = 11
    assert branch74(x, y) == 29