def branch1(param1, param2, param3):
    result = 0
    if param1 > 10:
        if param2 < 20:
            result = param1 * param2
        else:
            result = param1 + param2
    elif param1 <= 10:
        if param3 > 30:
            result = param1 * param3
        elif param3 <= 30 and param3 >= 10:
            result = param1 + param3
        else:
            result = param1 - param3
    else:
        result = param1 + param2 + param3
    return result