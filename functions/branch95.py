def branch95(user_input_1, user_input_2):
    """
    This function contains multiple branches depending on user inputs
    """

    if user_input_1 == 'yes':
        if user_input_2 == 'yes':
            return 'Both inputs are yes'
        else:
            return 'User input 1 is yes, user input 2 is no'
    elif user_input_1 == 'no':
        if user_input_2 == 'yes':
            return 'User input 1 is no, user input 2 is yes'
        else:
            return 'Both inputs are no'
    else:
        return 'Invalid user inputs'