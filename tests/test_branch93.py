from functions.branch93 import branch93
import pytest

@pytest.mark.parametrize("user_input, expected_output", [(1, "You chose branch 1"), (2, "You chose branch 2"), (3, "You chose branch 3"), (4, "You chose branch 4"), (5, "You chose branch 5"), (6, "You chose branch 6"), (7, "You chose branch 7"), (8, "You chose branch 8"), (9, "You chose branch 9"), (10, "You chose branch 10"), (11, "You chose an invalid branch!")])
def test_branch93(user_input, expected_output):
    assert branch93(user_input) == expected_output