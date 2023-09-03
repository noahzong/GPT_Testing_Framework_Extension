def branch77(x, y, z):
    """This function takes three user input parameters and returns a final value."""
    if x == 1:
        if y == 2:
            if z == 3:
                return "x, y, and z are all equal to 1, 2, and 3!"
            elif z > 3:
                return "x and y are equal to 1 and 2, and z is greater than 3!"
            else:
                return "x and y are equal to 1 and 2, and z is less than 3!"
        elif y > 2:
            if z == 3:
                return "x is equal to 1, y is greater than 2, and z is equal to 3!"
            elif z > 3:
                return "x is equal to 1, y is greater than 2, and z is greater than 3!"
            else:
                return "x is equal to 1, y is greater than 2, and z is less than 3!"
        else:
            if z == 3:
                return "x is equal to 1, y is less than 2, and z is equal to 3!"
            elif z > 3:
                return "x is equal to 1, y is less than 2, and z is greater than 3!"
            else:
                return "x is equal to 1, y is less than 2, and z is less than 3!"
    elif x > 1:
        if y == 2:
            if z == 3:
                return "x is greater than 1, y is equal to 2, and z is equal to 3!"
            elif z > 3:
                return "x is greater than 1, y is equal to 2, and z is greater than 3!"
            else:
                return "x is greater than 1, y is equal to 2, and z is less than 3!"
        elif y > 2:
            if z == 3:
                return "x is greater than 1, y is greater than 2, and z is equal to 3!"
            elif z > 3:
                return "x is greater than 1, y is greater than 2, and z is greater than 3!"
            else:
                return "x is greater than 1, y is greater than 2, and z is less than 3!"
        else:
            if z == 3:
                return "x is greater than 1, y is less than 2, and z is equal to 3!"
            elif z > 3:
                return "x is greater than 1, y is less than 2, and z is greater than 3!"
            else:
                return "x is greater than 1, y is less than 2, and z is less than 3!"
    else:
        if y == 2:
            if z == 3:
                return "x is less than 1, y is equal to 2, and z is equal to 3!"
            elif z > 3:
                return "x is less than 1, y is equal to 2, and z is greater than 3!"
            else:
                return "x is less than 1, y is equal to 2, and z is less than 3!"
        elif y > 2:
            if z == 3:
                return "x is less than 1, y is greater than 2, and z is equal to 3!"
            elif z > 3:
                return "x is less than 1, y is greater than 2, and z is greater than 3!"
            else:
                return "x is less than 1, y is greater than 2, and z is less than 3!"
        else:
            if z == 3:
                return "x is less than 1, y is less than 2, and z is equal to 3!"
            elif z > 3:
                return "x is less than 1, y is less than 2, and z is greater than 3!"
            else:
                return "x is less than 1, y is less than 2, and z is less than 3!"