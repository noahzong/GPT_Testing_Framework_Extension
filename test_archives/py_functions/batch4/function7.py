def function7(int1, str1, float1, list1):
    result = int1 * float1
    for item in list1:
        result += str1.count(item)
    return result