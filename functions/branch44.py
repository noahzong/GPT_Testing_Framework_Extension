def branch44(a, b, c, d):
    if a == 0 and b == 0:
        return 0
    elif a != 0 and b == 0:
        return c + d
    elif a == 0 and b != 0:
        return c * d
    elif a != 0 and b != 0:
        return c / d
    else:
        return c - d