def branch52(a, b, c):
    if a > 0:
        if b > 0:
            if c > 0:
                return a + b + c
            else:
                return a * b
        else:
            if c > 0:
                return a - c
            else:
                return a / b
    else:
        if b > 0:
            if c > 0:
                return b - c
            else:
                return b / a
        else:
            if c > 0:
                return c * a
            else:
                return a + b - c