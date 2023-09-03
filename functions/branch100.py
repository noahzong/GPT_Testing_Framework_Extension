def branch100(num1, num2, num3):
    """This function is an example of a function with a lot of branches.
    
    Parameters:
    num1 (int): a number
    num2 (int): a number
    num3 (int): a number
    
    Returns:
    int: a result based on the branching logic
    """
    if num1 == 0 and num2 == 0 and num3 == 0:
        result = 0
    elif num1 == 0 and num2 == 0 and num3 != 0:
        result = num3
    elif num1 == 0 and num2 != 0 and num3 == 0:
        result = num2
    elif num1 != 0 and num2 == 0 and num3 == 0:
        result = num1
    elif num1 == 0 and num2 != 0 and num3 != 0:
        result = num2 + num3
    elif num1 != 0 and num2 == 0 and num3 != 0:
        result = num1 + num3
    elif num1 != 0 and num2 != 0 and num3 == 0:
        result = num1 + num2
    else:
        result = num1 + num2 + num3
    return result