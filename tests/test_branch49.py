from functions.branch49 import branch49
import pytest

@pytest.mark.parametrize("user_input1, user_input2, expected_output", [
    ("A", "B", "Option 1"),
    ("A", "C", "Option 2"),
    ("A", "D", "Option 3"),
    ("B", "A", "Option 4"),
    ("B", "C", "Option 5"),
    ("B", "D", "Option 6"),
    ("C", "A", "Option 7"),
    ("C", "B", "Option 8"),
    ("C", "C", "Option 9"),
])
def test_branch49(user_input1, user_input2, expected_output):
    assert branch49(user_input1, user_input2) == expected_output