from functions.branch60 import branch60
import pytest

@pytest.mark.parametrize("input1, input2, expected", [
    (1, 2, -1),
    (2, 1, 1),
    (2, 2, 0)
])
def test_branch60(input1, input2, expected):
    assert branch60(input1, input2) == expected