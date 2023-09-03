def branch15(user_input1, user_input2):
    '''
    This function has a lot of branches
    '''
    output = None
    if user_input1 == 1:
        if user_input2 == 1:
            output = 'a'
        elif user_input2 == 2:
            output = 'b'
        else:
            output = 'c'
    elif user_input1 == 2:
        if user_input2 == 1:
            output = 'd'
        elif user_input2 == 2:
            output = 'e'
        else:
            output = 'f'
    elif user_input1 == 3:
        if user_input2 == 1:
            output = 'g'
        elif user_input2 == 2:
            output = 'h'
        else:
            output = 'i'
    else:
        output = 'j'
    
    return output