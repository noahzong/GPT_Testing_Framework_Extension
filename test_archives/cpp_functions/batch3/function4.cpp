;

# Translated C++ code
#include <iostream>
using namespace std;

int function4(int int1, int int2, float float1, float float2, string str1, string str2, bool bool1, bool bool2) {
    
    // Perform calculations
    int result1 = int1 + int2;
    float result2 = float1 + float2;
    
    // Concatenate strings
    string result3 = str1 + str2;
    
    // Perform boolean checks
    bool result4;
    if (bool1 == true && bool2 == true) {
        result4 = true;
    } else {
        result4 = false;
    }
    
    // Return final result
    return result1 + result2 + result3 + result4;
}