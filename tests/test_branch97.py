from functions.branch97 import branch97
import pytest

@pytest.mark.parametrize("user_input1, user_input2, expected", [
    ("A", "B", "Result 1"),
    ("A", "C", "Result 2"),
    ("A", "D", "Result 3"),
    ("D", "E", "Result 4"),
    ("D", "F", "Result 5"),
    ("D", "G", "Result 6"),
    ("E", "H", "Result 7"),
])
def test_branch97(user_input1, user_input2, expected):
    actual = branch97(user_input1, user_input2)
    assert expected == actual