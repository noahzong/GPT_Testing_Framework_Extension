#include <string>
#include <vector>

int function1(std::string string1, std::vector<int> list1, int int1=10) {
    // This is a sample function with a lot of variables and data types.
    // :param str string1: a string input
    // :param list list1: a list input
    // :param int int1: an optional int input with default value 10
    // :return: the multiplication of the string length, list length, and int
    // :rtype: int
    return string1.length() * list1.size() * int1;
}