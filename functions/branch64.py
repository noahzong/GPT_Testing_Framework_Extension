def branch64(x, y, z):
    if x > 10:
        if y > 10:
            if z == 0:
                return 0
            elif z < 0:
                return 1
            elif z > 0:
                return 2
        elif y < 10:
            if z == 0:
                return 3
            elif z < 0:
                return 4
            elif z > 0:
                return 5
    elif x < 10:
        if y > 10:
            if z == 0:
                return 6
            elif z < 0:
                return 7
            elif z > 0:
                return 8
        elif y < 10:
            if z == 0:
                return 9
            elif z < 0:
                return 10
            elif z > 0:
                return 11