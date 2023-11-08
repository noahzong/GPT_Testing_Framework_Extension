from functions.function1 import function1
import pytest

@pytest.fixture
def setup_function1():
    return function1('hello', 3, 4.5, True, [2, 4, 6])

def test_compute(setup_function1):
    assert setup_function1.compute() == 'hello34.5True[2, 4, 6]'