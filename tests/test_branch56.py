from functions.branch56 import branch56
import pytest

@pytest.mark.parametrize("input1, input2, expected", [
    (5, 2, 0.5),
    (1, 1, 0),
    (2, 5, -15)
])
def test_branch56(input1, input2, expected):
    assert branch56(input1, input2) == expected