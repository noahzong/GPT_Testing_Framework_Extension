from functions.branch3 import branch3
import pytest

@pytest.mark.parametrize("x, result", [
    (-20, "Very Negative"),
    (-5, "Negative"),
    (0, "Zero"),
    (2, "Very Small"),
    (7, "Small"),
    (12, "Medium Small"),
    (18, "Medium"),
    (22, "Medium Large"),
    (27, "Large"),
    (45, "Very Large"),
    (60, "Extremely Large")
])
def test_branch3(x, result):
    assert branch3(x) == result