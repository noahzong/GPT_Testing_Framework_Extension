from functions.branch20 import branch20
import pytest

def test_branch20_x0y0z0():
    assert branch20(0, 0, 0) == 0

def test_branch20_x0y0z1():
    assert branch20(0, 0, 1) == 1

def test_branch20_x0y1z0():
    assert branch20(0, 1, 0) == 2

def test_branch20_x0y1z1():
    assert branch20(0, 1, 1) == 2

def test_branch20_x1y0z0():
    assert branch20(1, 0, 0) == 3

def test_branch20_x1y0z1():
    assert branch20(1, 0, 1) == 4

def test_branch20_x1y1z0():
    assert branch20(1, 1, 0) == 5

def test_branch20_x1y1z1():
    assert branch20(1, 1, 1) == 5