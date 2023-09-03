def branch83(a, b):
    c = 0
    
    if a > 0:
        if b > 0:
            c = a + b
        elif b < 0:
            c = a - b
        else:
            c = a
    elif a < 0:
        if b > 0:
            c = a - b
        elif b < 0:
            c = a + b
        else:
            c = -a
    else:
        if b > 0:
            c = b
        elif b < 0:
            c = -b
        else:
            c = 0
    
    return c