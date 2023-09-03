from functions.branch23 import branch23
import pytest

@pytest.mark.parametrize('user_input1, user_input2, expected',
[(1, 2, 3), (1, 3, 4), (2, 3, 5), (2, 4, 6), (3, 4, 7)])
def test_branch23(user_input1, user_input2, expected):
    assert branch23(user_input1, user_input2) == expected