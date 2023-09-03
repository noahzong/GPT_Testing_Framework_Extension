def branch59(x1,x2):
    if x1 == 0:
        if x2 == 0:
            return 0
        else:
            return x2
    elif x1 < 0:
        if x2 == 0:
            return x1
        elif x2 > 0:
            return x1 + x2
        else:
            return -1
    else:
        if x2 == 0:
            return x1 * x2
        elif x2 > 0:
            return x1 - x2
        else:
            return x1 * x2