def function2(string1, int1, list1):
    """
    This function takes in 3 parameters: a string, an integer, and a list. It returns the sum of the integer and the length of the string.
    """
    result = int1 + len(string1)
    for item in list1:
        result += item
    return result