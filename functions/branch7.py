def branch7(x, y, z):
    if x > 0:
        if y > 0:
            result = x + y
        else:
            if z > 0:
                result = x + z
            else:
                result = x
    else:
        if y > 0:
            if z > 0:
                result = y + z
            else:
                result = y
        else:
            result = z
    
    if result % 2 == 0:
        result *= 2
    else:
        result -= 1
    
    if result > 10:
        return "Result is greater than 10"
    elif result < 0:
        return "Result is negative"
    else:
        return result