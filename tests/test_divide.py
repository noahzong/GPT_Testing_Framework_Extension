from functions.divide import divide
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_integers():
    assert divide(4,2) == 2
    assert divide(17,3) == 5.666666666666667

def test_divide_floats():
    assert divide(3.5, 1.5) == 2.3333333333333335