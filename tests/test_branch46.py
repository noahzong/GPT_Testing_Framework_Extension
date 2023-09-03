from functions.branch46 import branch46
import pytest

@pytest.mark.parametrize("var1, var2, expected_output", [
    ("high", "low", "Result1"),
    ("high", "medium", "Result2"),
    ("high", "high", "Result3"),
    ("medium", "low", "Result4"),
    ("medium", "medium", "Result5"),
    ("medium", "high", "Result6"),
    ("low", "low", "Result7"),
    ("low", "medium", "Result8"),
    ("low", "high", "Result9"),
])
def test_branch46(var1, var2, expected_output):
    assert branch46(var1, var2) == expected_output