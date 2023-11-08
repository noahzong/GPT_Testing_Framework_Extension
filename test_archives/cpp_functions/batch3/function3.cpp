# C++ Code
#include <iostream> 
#include <vector>
#include <map>
using namespace std;

float function3(int input1, float input2, string input3) {
    // Initialize variables
    bool boolean_var = true;
    int int_var = 5;
    float float_var = 5.0;
    vector<int> list_var = {1, 2, 3};
    map<string, int> dict_var = {{"name", "John"}, {"age", 20}};
    
    // Perform calculations
    float result1 = input1 + int_var;
    float result2 = result1 * float_var;
    float result3 = result2 / input2;
    
    // Process inputs
    if (boolean_var) {
        for (int item : list_var) {
            result3 += item;
        }
    }
    
    // Return the result
    return result3 + dict_var[input3];
}