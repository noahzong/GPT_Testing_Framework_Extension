from functions.branch4 import branch4
import pytest

@pytest.mark.parametrize("input_1, input_2, input_3, expected", [
    (5, 0, "yes", 10.0),
    (15, 200, "no", 235.0),
    (0, -20, "maybe", -15.0)
])
def test_branch4(input_1, input_2, input_3, expected):
    assert branch4(input_1, input_2, input_3) == expected