from functions.branch10 import branch10
import pytest

@pytest.mark.parametrize("a, b, operation, expected", [
    (1, 2, 'add', "Result is positive and greater than or equal to 10"),
    (2, 2, 'subtract', "Result is zero"),
    (3, 3, 'multiply', "Result is positive and greater than or equal to 10"),
    (10, 2, 'divide', "Result is positive and less than 10"),
    (5, 0, 'divide', "Cannot divide by zero!"),
    (2, 5, 'invalid', "Invalid operation")
])
def test_branch10(a, b, operation, expected):
    assert branch10(a, b, operation) == expected