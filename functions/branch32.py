def branch32 (x, y) :
    if x + y == 0:
        return 0
    elif x == 0:
        return y
    elif y == 0:
        return x
    else:
        return x + y + (x * y)