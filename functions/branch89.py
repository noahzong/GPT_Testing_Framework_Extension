def branch89(user_input1, user_input2):
    if user_input1 == 'A':
        if user_input2 == '1':
            return 'Option A1 has been chosen'
        elif user_input2 == '2':
            return 'Option A2 has been chosen'
        else:
            return 'No valid option chosen'
    elif user_input1 == 'B':
        if user_input2 == '1':
            return 'Option B1 has been chosen'
        elif user_input2 == '2':
            return 'Option B2 has been chosen'
        else:
            return 'No valid option chosen'
    else:
        return 'No valid option chosen'