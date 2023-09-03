def branch86(x, y):
    # if statement to check if x is equal to 0
    if x == 0:
        # if x is equal to 0, check if y is equal to 0
        if y == 0:
            return 0
        # if y is not equal to 0, return y
        else:
            return y
    # if x is not equal to 0, check if y is equal to 0
    elif y == 0:
        # if y is equal to 0, return x
        return x
    # if x and y are not equal to 0, multiply them
    else:
        return x * y