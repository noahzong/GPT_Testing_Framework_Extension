from functions.branch31 import branch31
import pytest

def test_branch31_a0():
    assert branch31(0, 0, 0) == 0

def test_branch31_a1_b0():
    assert branch31(1, 0, 0) == 1

def test_branch31_a1_b1_c0():
    assert branch31(1, 1, 0) == 2

def test_branch31_a1_b1_c1():
    assert branch31(1, 1, 1) == 3

def test_branch31_a2_b0_c0():
    assert branch31(2, 0, 0) == 4

def test_branch31_a2_b0_c1():
    assert branch31(2, 0, 1) == 5

def test_branch31_a2_b1():
    assert branch31(2, 1, 0) == 6

def test_branch31_a3_b0_c0():
    assert branch31(3, 0, 0) == 7

def test_branch31_a3_b0_c1():
    assert branch31(3, 0, 1) == 8

def test_branch31_a3_b1_c0():
    assert branch31(3, 1, 0) == 9

def test_branch31_a3_b1_c1():
    assert branch31(3, 1, 1) == 10