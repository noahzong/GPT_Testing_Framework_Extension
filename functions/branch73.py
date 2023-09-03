def branch73(x, y, z):
    # Initialize a variable
    result = 0
    
    # Check for first condition
    if x < y:
        # Check for second condition
        if y < z:
            # Calculate result
            result = x + y + z
        else:
            # Calculate result
            result = x + (2 * y) - z
    else:
        # Check for second condition
        if x == y:
            # Calculate result
            result = x + y + (2 * z)
        else:
            # Calculate result
            result = x * y * z
    
    # Return the result
    return result