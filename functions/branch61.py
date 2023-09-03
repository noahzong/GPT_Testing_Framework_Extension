def branch61(x, y):
    if x == 0 or y == 0:
        return 0
    elif x > 0 and y > 0:
        return x + y
    elif x < 0 and y < 0:
        return x - y
    elif x > 0 and y < 0:
        return x * y
    elif x < 0 and y > 0:
        return x / y
    else:
        return "Error"