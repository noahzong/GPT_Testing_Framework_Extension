from functions.divide import divide
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)

def test_divide_by_nonzero():
    assert divide(2, 1) == 2