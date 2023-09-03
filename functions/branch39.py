def branch39(input1, input2):
    # define a variable, result, to store the final result
    result = 0
    
    # if the first input is a number
    if type(input1) == int:
        # if the second input is a string
        if type(input2) == str:
            # if the string is longer than 5 characters
            if len(input2) > 5:
                # multiply the two inputs
                result = input1 * len(input2)
            else:
                # add the two inputs
                result = input1 + len(input2)
        
        # if the second input is not a string
        else:
            # add the two inputs
            result = input1 + input2
    
    # if the first input is not a number
    else:
        # if the second input is a string
        if type(input2) == str:
            # if the string is longer than 5 characters
            if len(input2) > 5:
                # multiply the length of the string with 10
                result = len(input2) * 10
            else:
                # multiply the length of the string with 5
                result = len(input2) * 5
            
        # if the second input is not a string
        else:
            # subtract the two inputs
            result = input1 - input2
    
    # return the result    
    return result