def branch42(x, y, z):
    if x == 0:
        if y == 0:
            if z == 0:
                return 'Zero'
            else:
                return 'Positive'
        else:
            if z == 0:
                return 'Negative'
            else:
                return 'Positive'
    else:
        if y == 0:
            if z == 0:
                return 'Positive'
            else:
                return 'Negative'
        else:
            if z == 0:
                return 'Positive'
            else:
                return 'Negative'