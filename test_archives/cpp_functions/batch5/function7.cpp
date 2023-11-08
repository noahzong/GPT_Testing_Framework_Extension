# C++ Code
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

class function7 {
public:
    function7(string user_input1, string user_input2, string user_input3) {
        this->user_input1 = user_input1;
        this->user_input2 = user_input2;
        this->user_input3 = user_input3;
        this->string1 = "";
        this->list1 = {};
        this->int1 = 0;
        this->float1 = 0.0;
        this->dict1 = {};
        this->boolean1 = false;
    }
    
    void method1() {
        this->string1 = this->user_input1 + this->user_input2;
        this->list1 = {this->user_input1, this->user_input2, this->user_input3};
        this->int1 = this->list1.size();
        this->float1 = this->int1 / 2;
        this->dict1 = { {this->user_input1, this->user_input2}, {this->user_input2, this->user_input3} };
        this->boolean1 = true;
    }
    
    string method2() {
        string final_value = this->string1 + to_string(this->int1) + to_string(this->float1) + to_string(this->dict1);
        return final_value;
    }
    
    string user_input1;
    string user_input2;
    string user_input3;
    string string1;
    vector<string> list1;
    int int1;
    float float1;
    unordered_map<string, string> dict1;
    bool boolean1;
};