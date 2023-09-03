def branch33(input1, input2):
    """A function with a lot of branches.

    Parameters:
    input1 (int): first user input
    input2 (str): second user input

    Returns:
    str: the result of the branches
    """
    if input1 > 0:
        if input2 == 'a':
            return 'Result A'
        elif input2 == 'b':
            return 'Result B'
        else:
            return 'Result C'
    else:
        if input2 == 'a':
            return 'Result D'
        elif input2 == 'b':
            return 'Result E'
        else:
            return 'Result F'