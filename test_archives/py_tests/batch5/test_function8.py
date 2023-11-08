from functions.function8 import function8
import pytest

@pytest.fixture
def function8_test():
    return function8(1, 2, 3)

def test_combine_vars(function8_test):
    assert function8_test.combine_vars() == "variable00.0False[](){}123"