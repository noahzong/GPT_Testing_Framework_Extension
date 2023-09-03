def branch69(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return 0
            else:
                return 1
        elif b == 1:
            return 2
        else:
            return 3
    elif a == 1:
        if b == 0:
            return 4
        elif b == 1:
            if c == 0:
                return 5
            else:
                return 6
        else:
            return 7
    else:
        if b == 0:
            return 8
        elif b == 1:
            return 9
        else:
            if c == 0:
                return 10
            else:
                return 11