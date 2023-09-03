def branch87(x, y):
    if x > 0 and y > 0:
        return x + y
    elif x < 0 and y < 0:
        return x - y
    elif x == 0 and y == 0:
        return 0
    elif x > 0 and y < 0:
        return x - abs(y)
    elif x < 0 and y > 0:
        return -1 * (abs(x) + y)
    else:
        return x + y