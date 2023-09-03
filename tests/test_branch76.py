from functions.branch76 import branch76
import pytest

@pytest.mark.parametrize(
    'x, y, z, expected', 
    [
        (10, 20, 30, 60), 
        (10, 20, 0, 200), 
        (10, 0, 30, 40),
        (10, 0, 0, 10),
        (0, 20, 30, 600),
        (0, 20, 0, 20),
        (0, 0, 30, 30),
        (0, 0, 0, 0)
    ]
)
def test_branch76(x, y, z, expected):
    assert branch76(x, y, z) == expected