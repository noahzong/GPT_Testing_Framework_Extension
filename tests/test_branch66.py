from functions.branch66 import branch66
import pytest

def test_branch66_positive_yes():
    assert branch66(1, 'yes') == 'positive'

def test_branch66_positive_no():
    assert branch66(1, 'no') == 'positive but negative'

def test_branch66_negative_yes():
    assert branch66(-1, 'yes') == 'negative but positive'

def test_branch66_negative_no():
    assert branch66(-1, 'no') == 'negative'

def test_branch66_invalid_input():
    assert branch66(0, 'maybe') == 'invalid input'