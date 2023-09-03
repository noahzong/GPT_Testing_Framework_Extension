def branch30(x, y, z):
    #x, y, and z are user input
    
    if x < 0:
        if y > 10:
            if z == 0:
                return -1
            else:
                return 0
        elif y < 10:
            if z > 0:
                return 1
            else:
                return 2
    elif x > 0:
        if y > 10:
            if z == 0:
                return 3
            else:
                return 4
        elif y < 10:
            if z > 0:
                return 5
            else:
                return 6
    else:
        return 7