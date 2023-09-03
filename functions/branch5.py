def branch5(num1, num2):
    if num1 > num2:
        result = num1 + num2
    elif num1 < num2:
        result = num1 - num2
    else:
        if num1 % 2 == 0:
            result = num1 * num2
        else:
            result = num1 ** num2

    if result >= 0:
        final_result = result
    else:
        final_result = abs(result)

    return final_result