def branch65(x, y):
    if x == 0 and y == 0:
        return 0
    elif x == 0 and y > 0:
        return y
    elif x > 0 and y == 0:
        return x
    elif x > 0 and y > 0:
        return x * y
    elif x < 0 and y == 0:
        return -x
    elif x < 0 and y > 0:
        return x + y
    elif x == 0 and y < 0:
        return -y
    elif x > 0 and y < 0:
        return x - y
    elif x < 0 and y < 0:
        return x / y