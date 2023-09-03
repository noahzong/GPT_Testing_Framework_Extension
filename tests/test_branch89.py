from functions.branch89 import branch89
import pytest

def test_branch89_A1():
    assert branch89('A', '1') == 'Option A1 has been chosen'

def test_branch89_A2():
    assert branch89('A', '2') == 'Option A2 has been chosen'

def test_branch89_B1():
    assert branch89('B', '1') == 'Option B1 has been chosen'

def test_branch89_B2():
    assert branch89('B', '2') == 'Option B2 has been chosen'

def test_branch89_wrongInput1():
    assert branch89('C', '1') == 'No valid option chosen'

def test_branch89_wrongInput2():
    assert branch89('A', '3') == 'No valid option chosen'

def test_branch89_wrongInput3():
    assert branch89('C', '3') == 'No valid option chosen'