from functions.branch71 import branch71
import pytest

@pytest.mark.parametrize("userInput1, userInput2, expected", [
    ("a", "b", "1"),
    ("a", "f", "2"),
    ("c", "d", "3"),
    ("c", "e", "4"),
    ("f", "e", "5"),
    ("f", "d", "6")
])
def test_branch71(userInput1, userInput2, expected):
    assert branch71(userInput1, userInput2) == expected