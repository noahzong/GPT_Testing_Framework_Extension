def function6(a, b, c, d, e):
    """
    This function takes in five arguments:
    a (string)
    b (integer)
    c (list)
    d (float)
    e (boolean)
   
    and returns the product of all the arguments.
    """
    product = a * b * d
    for x in c:
        product *= x
    if e:
        product *= 2
    return product