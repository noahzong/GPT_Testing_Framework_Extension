def branch99(x, y):
    if x == 0:
        if y == 0:
            return 0
        else:
            return y
    else:
        if y == 0:
            return x
        else:
            return x * y