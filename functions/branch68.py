def branch68(num1, num2, num3):

    # Initialize variables
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0

    # Branches
    if num1 > 0:
        total1 = num1 * 2
    elif num1 < 0:
        total1 = num1 * -2
    else:
        total1 = 0
    
    if num2 > 0:
        total2 = num2 * 3
    elif num2 < 0:
        total2 = num2 * -3
    else:
        total2 = 0
    
    if num3 > 0:
        total3 = num3 * 4
    elif num3 < 0:
        total3 = num3 * -4
    else:
        total3 = 0
    
    # Final total
    total4 = total1 + total2 + total3
    
    # Return value
    return total4