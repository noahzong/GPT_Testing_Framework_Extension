def function4(int1, int2, float1, float2, str1, str2, bool1, bool2):
    
    # Perform calculations
    result1 = int1 + int2
    result2 = float1 + float2
    
    # Concatenate strings
    result3 = str1 + str2
    
    # Perform boolean checks
    if bool1 == True and bool2 == True:
        result4 = True
    else:
        result4 = False
    
    # Return final result
    return result1 + result2 + result3 + result4