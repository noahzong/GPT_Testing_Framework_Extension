from functions.branch18 import branch18
import pytest

@pytest.mark.parametrize(
    'x, y, z, expected',
    [
        (1, 0, 0, 2),
        (1, 1, 0, 2),
        (1, 1, 1, 3),
        (0, 1, 1, 0),
        (0, 1, 0, 1),
        (0, -1, 0, -1),
        (0, -1, 1, 0),
        (-1, 1, 0, -1),
        (-1, 1, 1, 1),
        (-1, -1, 0, 1),
        (-1, -1, 1, 0),
        (1, -1, 0, 0),
        (1, -1, 1, 0),
        (0, 0, 0, 'No result.')
    ]
)
def test_branch18(x, y, z, expected):
    assert branch18(x, y, z) == expected