def branch49(user_input1, user_input2):
    if user_input1 == "A":
        if user_input2 == "B":
            return "Option 1"
        elif user_input2 == "C":
            return "Option 2"
        else:
            return "Option 3"
    elif user_input1 == "B":
        if user_input2 == "A":
            return "Option 4"
        elif user_input2 == "C":
            return "Option 5"
        else:
            return "Option 6"
    else:
        if user_input2 == "A":
            return "Option 7"
        elif user_input2 == "B":
            return "Option 8"
        else:
            return "Option 9"