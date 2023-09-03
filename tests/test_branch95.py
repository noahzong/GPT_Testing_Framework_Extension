from functions.branch95 import branch95
import pytest

@pytest.mark.parametrize("user_input_1, user_input_2, expected", [
    ('yes', 'yes', 'Both inputs are yes'),
    ('yes', 'no', 'User input 1 is yes, user input 2 is no'),
    ('no', 'yes', 'User input 1 is no, user input 2 is yes'),
    ('no', 'no', 'Both inputs are no'),
    ('invalid', 'input', 'Invalid user inputs')
])
def test_branch95(user_input_1, user_input_2, expected):
    """
    Test for branch95 function with 100% code coverage
    """
    assert branch95(user_input_1, user_input_2) == expected