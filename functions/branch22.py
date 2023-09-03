def branch22(num1, num2, num3):
    '''
    A function with a lot of branches.
    '''
    if num1 == 0:
        if num2 == 0:
            if num3 == 0:
                result = 0
            else:
                result = 1
        elif num3 == 0:
            result = 2
        else:
            result = 3
    elif num2 == 0:
        if num3 == 0:
            result = 4
        else:
            result = 5
    elif num3 == 0:
        result = 6
    else:
        result = 7
    return result