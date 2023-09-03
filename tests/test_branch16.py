from functions.branch16 import branch16
import pytest

@pytest.mark.parametrize("in_1, in_2, in_3, expected", 
[
    (1, 2, 2, 6),
    (2, 4, 2, 0),
    (3, 3, 3, 24),
    (4, 10, 5, 2)
])
def test_branch16(in_1, in_2, in_3, expected):
    assert branch16(in_1, in_2, in_3) == expected