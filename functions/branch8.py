def branch8(input_value):
    if input_value > 100:
        result = input_value * 2
    elif input_value <= 100 and input_value > 50:
        result = input_value + 50
    else:
        if input_value % 2 == 0:
            result = input_value // 2
        else:
            result = input_value * 3
    
    if result > 200:
        return result, "Result is greater than 200"
    elif result > 100:
        return result, "Result is between 100 and 200"
    else:
        return result, "Result is less than or equal to 100"