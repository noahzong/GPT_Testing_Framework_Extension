#C++ Code
#include <string>
#include <map>

std::string function3(std::string str1, int num1, std::map<int,int> dict1, bool bool1)
{
    //Store the sum of all the values in the dictionary
    int sum_dict1 = 0;
    for (auto const& value: dict1)
    {
        sum_dict1 += value.second;
    }

    //Calculate the final value
    std::string final_val = str1 + std::to_string(num1) + std::to_string(sum_dict1) + std::to_string(bool1);

    return final_val;
}