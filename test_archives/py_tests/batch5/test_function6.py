from functions.function6 import function6
import pytest

@pytest.mark.parametrize('num1,num2,str1,str2,lst1,lst2,expected_sum,expected_concat,expected_lst_avg', [
    (1, 2, 'a', 'b', [1, 2], [3, 4], 3, 'ab', 2.5),
    (2, 3, 'c', 'd', [4, 5], [6, 7], 5, 'cd', 5.5),
    (3, 4, 'e', 'f', [7, 8], [9, 10], 7, 'ef', 8.5)
])
def test_function6(num1, num2, str1, str2, lst1, lst2, expected_sum, expected_concat, expected_lst_avg):
    f6 = function6(num1, num2, str1, str2, lst1, lst2)
    assert f6.get_sum() == expected_sum
    assert f6.get_concat() == expected_concat