from functions.branch15 import branch15
import pytest

@pytest.mark.parametrize("user_input1, user_input2, expected", [
    (1, 1, 'a'), (1, 2, 'b'), (1, 3, 'c'),
    (2, 1, 'd'), (2, 2, 'e'), (2, 3, 'f'),
    (3, 1, 'g'), (3, 2, 'h'), (3, 3, 'i'),
    (4, 1, 'j')
])
def test_branch15(user_input1, user_input2, expected):
    assert branch15(user_input1, user_input2) == expected