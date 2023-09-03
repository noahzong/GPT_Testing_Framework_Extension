def branch67(x, y, z):
 
    if x > 10:
        if y > 0 and y < 10:
            if z > 0 and z < 10:
                return x + y + z
            else:
                return x + y 
        else:
            return x
    elif x == 10:
        return x * y * z
    else:
        return x * y