from functions.branch42 import branch42
import pytest

@pytest.mark.parametrize("x, y, z, expected", [
    (0, 0, 0, 'Zero'),
    (0, 0, 1, 'Positive'),
    (0, 1, 0, 'Negative'),
    (0, 1, 1, 'Positive'),
    (1, 0, 0, 'Positive'),
    (1, 0, 1, 'Negative'),
    (1, 1, 0, 'Positive'),
    (1, 1, 1, 'Negative')
])
def test_branch42(x, y, z, expected):
    assert branch42(x, y, z) == expected