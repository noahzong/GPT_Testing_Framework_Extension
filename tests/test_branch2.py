from functions.branch2 import branch2
import pytest

def test_branch2_negative():
    assert branch2(-1) == "Negative"

def test_branch2_zero():
    assert branch2(0) == "Zero"

def test_branch2_small():
    assert branch2(5) == "Small"

def test_branch2_medium():
    assert branch2(15) == "Medium"

def test_branch2_large():
    assert branch2(25) == "Large"

def test_branch2_very_large():
    assert branch2(50) == "Very Large"