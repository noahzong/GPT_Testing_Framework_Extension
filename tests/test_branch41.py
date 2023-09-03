from functions.branch41 import branch41
import pytest

@pytest.mark.parametrize("user_input1, user_input2, expected_result", [
    ("option1", "option1", "result1"),
    ("option1", "option2", "result2"),
    ("option2", "option1", "result3"),
    ("option2", "option2", "result4"),
    ("invalid", "invalid", "Invalid input")
])
def test_branch41(user_input1, user_input2, expected_result):
    assert branch41(user_input1, user_input2) == expected_result