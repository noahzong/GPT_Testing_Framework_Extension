// C++ code

#include<string>
#include<vector>

std::string function8(std::string string, std::vector<int> list1, bool boolean, int int1, float float1) {
    // Create a result variable
    std::string result = "";
    
    // Check the boolean
    if (boolean) {
        // If boolean is true, concatenate the string and int
        result = string + std::to_string(int1);
    }
    else {
        // If boolean is false, concatenate the list and float
        result = std::to_string(list1) + std::to_string(float1);
    }
    
    // Return the result
    return result;
}