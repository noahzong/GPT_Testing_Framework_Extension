def branch27(input1, input2):
    if input1 == 0:
        if input2 == 0:
            return 0
        elif input2 == 1:
            return 1
        else:
            return 2
    elif input1 == 1:
        if input2 == 0:
            return 3
        elif input2 == 1:
            return 4
        else:
            return 5
    else:
        if input2 == 0:
            return 6
        elif input2 == 1:
            return 7
        else:
            return 8