def branch25 (user_input1, user_input2):

    # Initialize Variables
    result1 = 0
    result2 = 0
    flag = False

    # Check if user input1 is less than 10
    if user_input1 < 10:
        result1 = user_input1 + 5
    else:
        result1 = user_input1 - 5

    # Check if user input2 is greater than 10
    if user_input2 > 10:
        result2 = user_input2 + 5
    else:
        result2 = user_input2 - 5

    # Check if both user inputs are equal
    if user_input1 == user_input2:
        flag = True

    # Return combined results
    return result1, result2, flag