def branch63(input1, input2):
    if input1 == 1 and input2 == 1:
        return 0
    elif input1 == 1 and input2 == 2:
        return 1
    elif input1 == 1 and input2 == 3:
        return 2
    elif input1 == 2 and input2 == 1:
        return 3
    elif input1 == 2 and input2 == 2:
        return 4
    elif input1 == 2 and input2 == 3:
        return 5
    elif input1 == 3 and input2 == 1:
        return 6
    elif input1 == 3 and input2 == 2:
        return 7
    elif input1 == 3 and input2 == 3:
        return 8