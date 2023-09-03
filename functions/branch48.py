def branch48(x, y, z): 
    # x, y, and z are all integers
    
    # Create a variable to store the final result
    result = 0 
    
    # Branches based on x
    if x == 0: 
        result = x + y 
    
    elif x == 1:
        result = x * y 
    
    elif x == 2:
        result = x + z 
    
    elif x == 3:
        result = x * z 
    
    # Branches based on y
    if y == 0: 
        result = y + z 
    
    elif y == 1:
        result = y * z 
    
    elif y == 2:
        result = y + x 
    
    elif y == 3:
        result = y * x 
    
    # Branches based on z
    if z == 0: 
        result = z + x 
    
    elif z == 1:
        result = z * x 
    
    elif z == 2:
        result = z + y 
    
    elif z == 3:
        result = z * y 
    
    # Return the final result
    return result