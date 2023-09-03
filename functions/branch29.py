def branch29(x, y):
    """
    This function takes two parameters and returns a value based on a branching structure.
    """
    if x > 0 and y > 0:
        return x + y
    elif x > 0 and y <= 0:
        return x - y
    elif x <= 0 and y > 0:
        return y - x
    else:
        return x * y