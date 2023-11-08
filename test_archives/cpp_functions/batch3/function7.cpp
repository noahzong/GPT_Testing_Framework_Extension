# C++ Code
#include <string>
#include <vector>
#include <numeric>

using namespace std;

int function7(string string1, int number1, vector<int> list1) 
{
    // Calculate the length of the string
    int length_string = string1.length();
    
    // Multiply the number and the length of the string
    int result1 = number1 * length_string;
    
    // Iterate through the list and calculate the sum
    int result2 = accumulate(list1.begin(), list1.end(), 0);
    
    // Calculate the final result
    int final_result = result1 + result2;
    
    return final_result;
}