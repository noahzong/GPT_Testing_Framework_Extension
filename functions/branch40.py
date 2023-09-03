def branch40(num1, num2, num3, num4):
    if num1 > 0 and num2 > 0 and num3 > 0:
        result1 = num1 + num2 + num3
        if num4 > 0:
            result2 = result1 * num4
            return result2
        else:
            return result1
    elif num1 > 0 and num2 > 0 and num3 == 0:
        result3 = num1 - num2
        if num4 > 0:
            result4 = result3 / num4
            return result4
        else:
            return result3
    elif num1 > 0 and num2 == 0 and num3 > 0:
        result5 = num1 * num3
        if num4 > 0:
            result6 = result5 + num4
            return result6
        else:
            return result5
    elif num1 == 0 and num2 > 0 and num3 > 0:
        result7 = num2 - num3
        if num4 > 0:
            result8 = result7 * num4
            return result8
        else:
            return result7
    else:
        return 0