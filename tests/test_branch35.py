from functions.branch35 import branch35
import pytest

@pytest.mark.parametrize("user_input, expected", [
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
    ("F", "F"),
    ("G", "G"),
    ("H", "H"),
    ("I", False)
])
def test_branch35(user_input, expected):
    assert branch35(user_input) == expected