def branch12(x, y, z):
    '''
    This function takes in three parameters and returns a value
    based on a series of conditions.
    '''
    if x == 0:
        if y == 0:
            if z == 0:
                return 0
            elif z > 0:
                return 1
            else:
                return -1
        elif y > 0:
            if z == 0:
                return 2
            elif z > 0:
                return 3
            else:
                return 4
        else:
            if z == 0:
                return 5
            elif z > 0:
                return 6
            else:
                return 7
    elif x > 0:
        if y == 0:
            if z == 0:
                return 8
            elif z > 0:
                return 9
            else:
                return 10
        elif y > 0:
            if z == 0:
                return 11
            elif z > 0:
                return 12
            else:
                return 13
        else:
            if z == 0:
                return 14
            elif z > 0:
                return 15
            else:
                return 16
    else:
        if y == 0:
            if z == 0:
                return 17
            elif z > 0:
                return 18
            else:
                return 19
        elif y > 0:
            if z == 0:
                return 20
            elif z > 0:
                return 21
            else:
                return 22
        else:
            if z == 0:
                return 23
            elif z > 0:
                return 24
            else:
                return 25