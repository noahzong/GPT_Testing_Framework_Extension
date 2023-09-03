def branch14(x, y, z):
    result = 0
    if x > 0 and y > 0 and z > 0:
        result = 1
    elif x > 0 and y > 0 and z <= 0:
        result = 2
    elif x > 0 and y <= 0 and z > 0:
        result = 3
    elif x > 0 and y <= 0 and z <= 0:
        result = 4
    elif x <= 0 and y > 0 and z > 0:
        result = 5
    elif x <= 0 and y > 0 and z <= 0:
        result = 6
    elif x <= 0 and y <= 0 and z > 0:
        result = 7
    elif x <= 0 and y <= 0 and z <= 0:
        result = 8
    return result