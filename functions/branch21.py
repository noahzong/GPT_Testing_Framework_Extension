def branch21(num1, num2):
    if num1 == 0 and num2 == 0:
        return 0
    elif num1 == 0 and num2 != 0:
        return num2
    elif num1 != 0 and num2 == 0:
        return num1
    elif num1 > 0 and num2 > 0:
        return num1 + num2
    elif num1 < 0 and num2 < 0:
        return num1 * num2
    elif num1 > 0 and num2 < 0:
        return num1 - num2
    elif num1 < 0 and num2 > 0:
        return num2 - num1
    elif num1 == num2:
        return num1 * num2
    else:
        return 0