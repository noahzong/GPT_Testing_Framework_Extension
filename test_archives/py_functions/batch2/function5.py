def function5(int1, float1, str1, list1): 
    # This function takes in an integer, float, string and list as parameters
    # and returns the sum of the first two parameters
    result = int1 + float1

    # The string and list are used to construct a new list
    new_list = []
    for i in range(len(list1)):
        new_list.append(str1 + list1[i])

    # Return the sum of the first two parameters and the new list
    return result, new_list