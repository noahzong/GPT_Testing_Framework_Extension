from functions.function5 import function5
import pytest

@pytest.fixture
def test_class():
    test_class = function5('hello', 5, 3.4, True)
    return test_class

def test_process_data_1(test_class):
    assert test_class.process_data() == 56.0

def test_process_data_2(test_class):
    test_class.input_string = 'world'
    assert test_class.process_data() == 56.0