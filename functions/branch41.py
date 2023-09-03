def branch41(user_input1, user_input2):
    if user_input1 == "option1":
        if user_input2 == "option1":
            return "result1"
        elif user_input2 == "option2":
            return "result2"
    elif user_input1 == "option2":
        if user_input2 == "option1":
            return "result3"
        elif user_input2 == "option2":
            return "result4"
    else:
        return "Invalid input"