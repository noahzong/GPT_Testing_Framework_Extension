def function3(input1, input2, input3):
    """
    This function takes in 3 parameters - input1, input2, and input3 - 
    and returns a singular final value. 
    """
    
    # Initialize variables
    boolean_var = True
    int_var = 5
    float_var = 5.0
    list_var = [1, 2, 3]
    dict_var = {'name': 'John', 'age': 20}
    
    # Perform calculations
    result1 = input1 + int_var
    result2 = result1 * float_var
    result3 = result2 / input2
    
    # Process inputs
    if boolean_var:
        for item in list_var:
            result3 += item
    
    # Return the result
    return result3 + dict_var[input3]