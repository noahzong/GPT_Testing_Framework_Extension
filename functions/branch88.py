def branch88(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return 0
            else:
                return 1
        else:
            return 2
    else:
        if b == 0:
            if c == 0:
                return 3
            else:
                return 4
        else:
            if c == 0:
                return 5
            else:
                return 6