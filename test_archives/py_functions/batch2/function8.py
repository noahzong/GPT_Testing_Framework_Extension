def function8(string, list1, boolean, int1, float1):
    """
    This function takes in a string, list, boolean, integer, and float and returns a single final value
    """
    
    # Create a result variable
    result = ""
    
    # Check the boolean
    if boolean:
        # If boolean is true, concatenate the string and int
        result = string + str(int1)
    else:
        # If boolean is false, concatenate the list and float
        result = str(list1) + str(float1)
        
    # Return the result
    return result