def function1(string, number, boolean):
    result = string
    if boolean == True:
        result += number
    else:
        result += (number * 2)
    return result