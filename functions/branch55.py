def branch55(user_input1, user_input2):
    if user_input1 < 0:
        if user_input2 > 0:
            return user_input1 + user_input2
        elif user_input2 == 0:
            return user_input1
        else:
            return user_input1 - user_input2
    elif user_input1 == 0:
        if user_input2 > 0:
            return user_input2
        elif user_input2 == 0:
            return 0
        else:
            return user_input2 * -1
    else:
        if user_input2 > 0:
            return user_input1 - user_input2
        elif user_input2 == 0:
            return user_input1
        else:
            return user_input1 + user_input2