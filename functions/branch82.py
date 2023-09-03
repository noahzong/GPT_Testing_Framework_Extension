def branch82(x, y): 
    if x < 0: 
        if y > 0: 
            return x + y 
        else: 
            return x - y 
    elif x == 0: 
        return 0 
    else: 
        if y < 0: 
            return x - y 
        else: 
            return x + y