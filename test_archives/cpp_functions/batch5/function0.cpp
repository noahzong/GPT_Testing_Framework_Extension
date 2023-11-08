#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <tuple>

using namespace std;

class Function0 {
public:
    int integer;
    float float;
    string string;
    vector<int> list;
    map<char, int> dictionary;
    tuple<int, int, int> tuple;
    set<int> set;
    
    Function0(int int_input, float float_input, string string_input, vector<int> list_input) {
        integer = int_input;
        float = float_input;
        string = string_input;
        list = list_input;
        dictionary = {{'a', 1}, {'b', 2}, {'c', 3}};
        tuple = make_tuple(1, 2, 3);
        set = {1, 2, 3};
    }
    
    double multiply_result() {
        double result = integer * float;
        for (int i : list) {
            result *= i;
        }
        return result;
    }
};