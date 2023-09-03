def branch92(a,b,c,d,e):
    # Initialize variables
    x = 0
    y = 0
    
    # If-else branches
    if a > b:
        x = a * c
    else:
        x = b * c
        
    if d > e:
        y = d + e
    else:
        y = e + d
        
    # Return final values
    return x + y