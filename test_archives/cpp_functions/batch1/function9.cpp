// C++ code 

#include <string> 

std::string function9(std::string string, int number, bool boolean) { 
    // calculate a result based on the input parameters 
    std::string result = (string + std::to_string(number)) * boolean;
    return result; 
}