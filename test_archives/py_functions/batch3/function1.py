def function1(string1, int1, float1, list1): 
    my_string = string1 * int1  # my_string is a string
    my_float = float1 * len(list1)  # my_float is a float
    my_list = [x*float1 for x in list1]  # my_list is a list of floats
    my_total = my_string + my_float  # my_total is a float
    return my_total  # returns one singular final value