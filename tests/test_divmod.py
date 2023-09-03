from functions.divmod import divmod
import pytest

def test_divmod_with_zero_y():
    with pytest.raises(ZeroDivisionError):
        divmod(0, 0)

def test_divmod_with_positive_x_and_y():
    quotient, remainder = divmod(3, 2)
    assert quotient == 1
    assert remainder == 1

def test_divmod_with_negative_x_and_y():
    quotient, remainder = divmod(-3, 2)
    assert quotient == -2
    assert remainder == 1