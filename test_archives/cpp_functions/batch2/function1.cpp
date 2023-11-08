#include <string>

std::string function1(std::string string, int number, bool boolean) {
    std::string result = string;
    if (boolean == true) {
        result += std::to_string(number);
    }
    else {
        result += std::to_string(number * 2);
    }
    return result;
}