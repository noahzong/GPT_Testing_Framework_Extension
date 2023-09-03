def branch18(x, y, z):
    """This function takes three parameters and 
    returns a final value based on those parameters. 
    """
    if x > 0 and y == 0:
        return x + 1
    elif x > 0 and y > 0:
        return x + y + z
    elif x == 0 and y > 0:
        return x + y - z
    elif x < 0 and y > 0:
        return x * y + z
    elif x < 0 and y < 0:
        return x * y - z
    elif x == 0 and y < 0:
        return x - y + z
    elif x > 0 and y < 0:
        return x - y - z
    else:
        return "No result."