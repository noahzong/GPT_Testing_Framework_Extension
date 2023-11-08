def function3(str1, num1, dict1, bool1):
    """
    This function takes in four variables of type string, number, dictionary and boolean and returns a single value.
    """
    #Store the sum of all the values in the dictionary
    sum_dict1 = 0
    for value in dict1.values():
        sum_dict1 += value

    #Calculate the final value
    final_val = str1 + str(num1) + str(sum_dict1) + str(bool1)

    return final_val