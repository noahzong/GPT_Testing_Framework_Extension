# C++ Code
#include <vector>
#include <string>

std::pair<double, std::vector<std::string>> function5(int int1, float float1, std::string str1, std::vector<std::string> list1) {
    double result = int1 + float1;

    std::vector<std::string> new_list;
    for (int i = 0; i < list1.size(); i++) {
        new_list.push_back(str1 + list1[i]);
    }

    return std::make_pair(result, new_list);
}