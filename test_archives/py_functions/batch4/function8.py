def function8(int1,int2,str1,list1):
    new_list = []
    for i in list1:
        new_list.append(i+int1)
    final_int = int2 * int1
    final_str = str1 + str(final_int)
    return final_str, new_list

#test code
int1 = 3
int2 = 5
str1 = "The answer is "
list1 = [1,2,3]

function8(int1,int2,str1,list1)
# Output: ("The answer is 15", [4,5,6])