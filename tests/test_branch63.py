from functions.branch63 import branch63
import pytest

def test_branch_63_1_1():
    assert branch63(1,1) == 0

def test_branch_63_1_2():
    assert branch63(1,2) == 1

def test_branch_63_1_3():
    assert branch63(1,3) == 2

def test_branch_63_2_1():
    assert branch63(2,1) == 3

def test_branch_63_2_2():
    assert branch63(2,2) == 4

def test_branch_63_2_3():
    assert branch63(2,3) == 5

def test_branch_63_3_1():
    assert branch63(3,1) == 6

def test_branch_63_3_2():
    assert branch63(3,2) == 7

def test_branch_63_3_3():
    assert branch63(3,3) == 8