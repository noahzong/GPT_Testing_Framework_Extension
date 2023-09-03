def branch90(x, y, z):
    if x == 1:
        if y == 2:
            if z == 3:
                return 'Result 1'
            elif z == 4:
                return 'Result 2'
            else:
                return 'Result 3'
        elif y == 3:
            return 'Result 4'
        elif y == 4:
            return 'Result 5'
        else:
            return 'Result 6'
    elif x == 2:
        if y == 2:
            if z == 3:
                return 'Result 7'
            elif z == 4:
                return 'Result 8'
            else:
                return 'Result 9'
        elif y == 3:
            return 'Result 10'
        elif y == 4:
            return 'Result 11'
        else:
            return 'Result 12'
    else:
        return 'Result 13'