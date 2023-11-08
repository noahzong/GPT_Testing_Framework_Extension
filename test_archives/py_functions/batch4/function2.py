def function2(string, num1, num2, list_input):
    '''
    This function takes in four parameters: a string, two numerical values, and a list.
    It then uses those parameters to calculate a final numerical value.
    '''
    # Calculate the total length of the string
    string_len = len(string)
    
    # Calculate the total sum of the numerical values
    total_sum = num1 + num2
    
    # Calculate the total length of the list
    list_len = len(list_input)
    
    # Calculate the final numerical value
    final_val = (string_len * total_sum) / list_len
    
    return final_val