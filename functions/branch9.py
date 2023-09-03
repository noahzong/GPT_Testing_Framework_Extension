def branch9(a, b):
    if a > b:
        result = a + b
    elif a < b:
        if b % 2 == 0:
            result = a * b
        else:
            result = a - b
    else:
        if a % 2 == 0:
            result = a // b
        else:
            result = a ** b
    
    if result > 10:
        return result * 2
    elif result < 0:
        return result + 10
    else:
        return result