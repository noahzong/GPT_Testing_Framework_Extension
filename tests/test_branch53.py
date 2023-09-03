from functions.branch53 import branch53
import pytest

@pytest.mark.parametrize("num1, num2, char, expected", [
    (10, -5, 'a', 5),
    (-10, 5, 'b', -5),
    (-10, 5, 'c', -2),
    (10, -5, 'a', 5),
    (10, -5, 'b', 15),
    (10, -5, 'c', -50),
    (-10, 5, 'a', -15),
    (-10, 5, 'b', -5),
    (-10, 5, 'c', 2),
    (10, 5, 'a', 50),
    (10, 5, 'b', 2),
    (10, 5, 'c', 15),
    (10, 5, 'd', 'error')
])
def test_branch53(num1, num2, char, expected):
    assert branch53(num1, num2, char) == expected