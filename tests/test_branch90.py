from functions.branch90 import branch90
import pytest

@pytest.mark.parametrize('x, y, z, expected_result', [
    (1, 2, 3, 'Result 1'),
    (1, 2, 4, 'Result 2'),
    (1, 2, 5, 'Result 3'),
    (1, 3, 0, 'Result 4'),
    (1, 4, 0, 'Result 5'),
    (1, 5, 0, 'Result 6'),
    (2, 2, 3, 'Result 7'),
    (2, 2, 4, 'Result 8'),
    (2, 2, 5, 'Result 9'),
    (2, 3, 0, 'Result 10'),
    (2, 4, 0, 'Result 11'),
    (2, 5, 0, 'Result 12'),
    (3, 0, 0, 'Result 13')
])
def test_branch90(x, y, z, expected_result):
    assert branch90(x, y, z) == expected_result