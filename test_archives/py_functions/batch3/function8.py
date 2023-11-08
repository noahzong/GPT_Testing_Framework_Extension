def function8(num1, str1, bool1, num2):
    """
    This Function takes in four parameters, two numbers, a string, and a boolean.
    It returns the result of the two numbers added together if the boolean is true.
    Otherwise, it returns the length of the string.
    """
    if bool1:
        return num1 + num2
    else:
        return len(str1)