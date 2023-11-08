# C++ Code

#include <string>
#include <vector>

int function2(std::string string1, int int1, std::vector<int> list1) {
    int result = int1 + string1.length();
    for (int item : list1) {
        result += item;
    }
    return result;
}