def branch34(num1, num2):
    if num1 > 0 and num2 > 0:
        return num1 * num2
    elif num1 < 0 and num2 < 0:
        return num1 + num2
    elif num1 == 0 or num2 == 0:
        return 0
    else:
        return num1 - num2