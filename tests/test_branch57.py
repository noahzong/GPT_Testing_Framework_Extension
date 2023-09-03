from functions.branch57 import branch57
import pytest

@pytest.mark.parametrize("num1, num2, num3, expected", [
	(1,2,3, 3),
	(2,1,3, 3),
	(3,1,2, 3),
	(1,2,2, 2),
	(2,3,3, 3),
	(1,1,3, 1),
	(1,3,3, 3),
	(1,1,1, 1),
	(1,2,4, 4),
	(4,2,1, 4),
	(4,1,2, 4)
])
def test_branch57(num1, num2, num3, expected):
	assert branch57(num1, num2, num3) == expected