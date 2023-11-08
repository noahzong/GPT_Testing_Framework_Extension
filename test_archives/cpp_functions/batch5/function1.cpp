#include <string>
#include <list>
using namespace std;

class function1 {

public:
    string string1;
    int int1;
    float float1;
    bool boolean1;
    list<string> list1;

    function1(string string1, int int1, float float1, bool boolean1, list<string> list1) {
        this->string1 = string1;
        this->int1 = int1;
        this->float1 = float1;
        this->boolean1 = boolean1;
        this->list1 = list1;
    }

    string compute() {
        string final_value = string1 + to_string(int1) + to_string(float1) + to_string(boolean1) + to_string(list1);
        return final_value;
    }

};