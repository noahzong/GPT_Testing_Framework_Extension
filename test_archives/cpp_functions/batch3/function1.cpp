#include <string> 
#include <vector> 
#include <numeric>

using namespace std; 

float function1(string string1, int int1, float float1, vector<float> list1) { 
    string my_string = string1; 
    for (int i = 0; i < int1 - 1; i++) { 
        my_string += string1; 
    } 
    float my_float = float1 * list1.size(); 
    vector<float> my_list; 
    for (float x : list1) { 
        my_list.push_back(x * float1); 
    } 
    float my_total = my_string.length() + my_float; 
    return my_total; 
}