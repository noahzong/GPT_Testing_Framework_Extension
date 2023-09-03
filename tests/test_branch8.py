from functions.branch8 import branch8
import pytest

def test_branch8_greater_than_100():
    result, message = branch8(200)
    assert result == 400
    assert message == "Result is greater than 200"

def test_branch8_between_100_and_50():
    result, message = branch8(75)
    assert result == 125
    assert message == "Result is between 100 and 200"

def test_branch8_less_than_50_even():
    result, message = branch8(40)
    assert result == 20
    assert message == "Result is less than or equal to 100"

def test_branch8_less_than_50_odd():
    result, message = branch8(41)
    assert result == 123
    assert message == "Result is less than or equal to 100"