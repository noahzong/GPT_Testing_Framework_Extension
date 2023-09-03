def branch26(a, b, c):
    """This function uses a lot of branches to determine the outcome"""
    
    if a > b and a > c:
        result = a + b + c
    elif b > a and b > c:
        result = a * b * c
    elif c > a and c > b:
        result = a / b / c
    elif a == b and b == c:
        result = a ** b ** c
    else:
        result = 0
    
    return result