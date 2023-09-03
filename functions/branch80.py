def branch80(num1,num2,num3):
    # Initialize a variable to store the returned value 
    result = 0 
    
    # If num1 is greater than num2, add num3 to result
    if num1 > num2:
        result += num3 
    # If num1 is greater than or equal to num2, subtract num3 from result
    elif num1 >= num2:
        result -= num3
    # If num1 is equal to num2, multiply result by num3
    elif num1 == num2:
        result *= num3
    # If num1 is not greater than, greater than or equal to, or equal to num2, divide result by num3
    else:
        result /= num3 
    
    # Return the final result 
    return result