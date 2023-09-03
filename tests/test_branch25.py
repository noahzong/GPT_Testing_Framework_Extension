from functions.branch25 import branch25
import pytest
 
def test_branch25_user_input1_less_than_10():
    user_input1 = 5
    user_input2 = 15
    expected_result1 = 10
    expected_result2 = 20
    expected_flag = False
    
    result1, result2, flag = branch25(user_input1, user_input2)
    
    assert result1 == expected_result1
    assert result2 == expected_result2
    assert flag == expected_flag
 
def test_branch25_user_input1_greater_than_10():
    user_input1 = 15
    user_input2 = 5
    expected_result1 = 10
    expected_result2 = 0
    expected_flag = False
    
    result1, result2, flag = branch25(user_input1, user_input2)
    
    assert result1 == expected_result1
    assert result2 == expected_result2
    assert flag == expected_flag
 
def test_branch25_user_inputs_equal():
    user_input1 = 10
    user_input2 = 10
    expected_result1 = 5
    expected_result2 = 5
    expected_flag = True
    
    result1, result2, flag = branch25(user_input1, user_input2)
    
    assert result1 == expected_result1
    assert result2 == expected_result2
    assert flag == expected_flag