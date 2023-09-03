from functions.branch98 import branch98
import pytest

def test_branch98_positive_inputs():
    assert branch98(3, 4) == 7

def test_branch98_negative_inputs():
    assert branch98(-3, -4) == 7

def test_branch98_mixed_inputs():
    assert branch98(3, -4) == -1

def test_branch98_zeros_inputs():
    assert branch98(0, 0) == 0