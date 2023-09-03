from functions.branch12 import branch12
import pytest

def test_branch12_1():
    assert branch12(0, 0, 0) == 0
    
def test_branch12_2():
    assert branch12(0, 0, 1) == 1

def test_branch12_3():
    assert branch12(0, 0, -1) == -1

def test_branch12_4():
    assert branch12(0, 1, 0) == 2

def test_branch12_5():
    assert branch12(0, 1, 1) == 3

def test_branch12_6():
    assert branch12(0, 1, -1) == 4

def test_branch12_7():
    assert branch12(0, -1, 0) == 5

def test_branch12_8():
    assert branch12(0, -1, 1) == 6

def test_branch12_9():
    assert branch12(0, -1, -1) == 7

def test_branch12_10():
    assert branch12(1, 0, 0) == 8

def test_branch12_11():
    assert branch12(1, 0, 1) == 9

def test_branch12_12():
    assert branch12(1, 0, -1) == 10

def test_branch12_13():
    assert branch12(1, 1, 0) == 11

def test_branch12_14():
    assert branch12(1, 1, 1) == 12

def test_branch12_15():
    assert branch12(1, 1, -1) == 13

def test_branch12_16():
    assert branch12(1, -1, 0) == 14

def test_branch12_17():
    assert branch12(1, -1, 1) == 15

def test_branch12_18():
    assert branch12(1, -1, -1) == 16

def test_branch12_19():
    assert branch12(-1, 0, 0) == 17

def test_branch12_20():
    assert branch12(-1, 0, 1) == 18

def test_branch12_21():
    assert branch12(-1, 0, -1) == 19

def test_branch12_22():
    assert branch12(-1, 1, 0) == 20

def test_branch12_23():
    assert branch12(-1, 1, 1) == 21

def test_branch12_24():
    assert branch12(-1, 1, -1) == 22

def test_branch12_25():
    assert branch12(-1, -1, 0) == 23

def test_branch12_26():
    assert branch12(-1, -1, 1) == 24

def test_branch12_27():
    assert branch12(-1, -1, -1) == 25