def branch28(x, y):
    
    if (x > 0) and (y > 0):
        result = x + y
    elif (x < 0) and (y < 0):
        result = x * y
    elif (x > 0) and (y < 0):
        result = x - y
    elif (x < 0) and (y > 0):
        result = y - x
    elif (x == 0) and (y == 0):
        result = 0
    else:
        result = x + y + 1    
        
    return result