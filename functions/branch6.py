def branch6(a, b, c):
    if a > 10:
        if b < 5:
            result = a + b
        else:
            result = a - b
    elif a <= 10 and c == 'yes':
        result = a * b
    else:
        if c == 'no':
            result = a / b
        else:
            result = a % b
    
    return result