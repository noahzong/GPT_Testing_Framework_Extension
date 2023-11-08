from functions.function3 import function3
import pytest

@pytest.fixture
def function3():
    return function3('John', 25, 'Male', '123 Main Street', 555-555-5555)

def test_function3_init(function3):
    assert function3.name == 'John'
    assert function3.age == 25
    assert function3.gender == 'Male'
    assert function3.address == '123 Main Street'
    assert function3.phone_number == '555-555-5555'
  
def test_function3_calculate_value(function3):
    assert function3.calculate_value() == 25 + 555555555