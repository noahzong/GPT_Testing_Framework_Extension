# C++ Code
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

class function5 {
public:
    string input_string;
    int input_int;
    float input_float;
    bool input_bool;
    vector<int> list_1;
    vector<float> list_2;
    unordered_map<string, int> dict_1;
    unordered_map<string, float> dict_2;
    
    function5(string input_string, int input_int, float input_float, bool input_bool) {
        this->input_string = input_string;
        this->input_int = input_int;
        this->input_float = input_float;
        this->input_bool = input_bool;
    }

    float process_data() {
        float result = 0;
        for (int i = 0; i < input_int; i++) {
            result += input_float * (i + 1);
        }

        if (input_bool) {
            result += input_string.length();
        }

        return result;
    }
};