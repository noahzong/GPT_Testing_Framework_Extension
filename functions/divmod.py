def divmod(x, y):
    if y == 0:
        raise ZeroDivisionError("division by zero")
    quotient = x // y
    remainder = x % y
    return quotient, remainder