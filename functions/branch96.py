def branch96(a,b,c):
    
    # First branch
    if a == 0:
        x = b * c
    elif a == 1:
        x = b + c
    else:
        x = b - c
        
    # Second branch
    if x < 0:
        y = 0
    elif x == 0:
        y = 1
    else:
        y = x + 1
        
    # Third branch
    if y % 2 == 0:
        z = y + c
    else:
        z = y - c
        
    return z