def branch81(a, b, c):
    if a > 0:
        if b == c:
            return a + b
        else:
            return a - b
    else:
        if c > 0:
            return b + c
        else:
            return b - c