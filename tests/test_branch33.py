from functions.branch33 import branch33
import pytest

def test_branch33_positive_result_a():
    assert branch33(1, 'a') == 'Result A'

def test_branch33_positive_result_b():
    assert branch33(1, 'b') == 'Result B'

def test_branch33_positive_result_c():
    assert branch33(1, 'c') == 'Result C'

def test_branch33_negative_result_d():
    assert branch33(-1, 'a') == 'Result D'

def test_branch33_negative_result_e():
    assert branch33(-1, 'b') == 'Result E'

def test_branch33_negative_result_f():
    assert branch33(-1, 'c') == 'Result F'