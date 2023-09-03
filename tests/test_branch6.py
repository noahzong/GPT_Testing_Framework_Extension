from functions.branch6 import branch6
import pytest

@pytest.mark.parametrize("a, b, c, output", [  
    (11, 2, 'yes', 22),
    (11, 3, 'no', 3.6666666666666665),
    (10, 3, 'yes', 30),
    (7, 3, 'no', 2.3333333333333335),
    (7, 3, 'maybe', 1),
    (11, 3, 'maybe', 2)
])
def test_branch6(a, b, c, output):
    assert branch6(a, b, c) == output