def function3(string1, int1, float1):
    """This function takes in 3 parameters and returns a value. 
    Parameters:
    string1 (str): A string value
    int1 (int): An integer value
    float1 (float): A float value
    Returns:
    int2 (int): An integer value
    """
    int2 = int1 * float1
    if string1 == "yes":
        int2 += 10
    elif string1 == "no":
        int2 -= 5
    return int2