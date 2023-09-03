from functions.divide import divide
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)
        
def test_divide_non_zero():
    assert divide(3, 2) == 1.5