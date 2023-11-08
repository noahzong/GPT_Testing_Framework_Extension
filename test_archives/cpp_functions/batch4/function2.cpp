# Translated C++ code
#include <string>
#include <vector>
using namespace std;

double function2(string string, double num1, double num2, vector<double> list_input) {
    // Calculate the total length of the string
    int string_len = string.length();
    
    // Calculate the total sum of the numerical values
    double total_sum = num1 + num2;
    
    // Calculate the total length of the list
    int list_len = list_input.size();
    
    // Calculate the final numerical value
    double final_val = (string_len * total_sum) / list_len;
    
    return final_val;
}