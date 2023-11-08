#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

class function4{
public:
    string name;
    int age;
    string gender;
    int income;
    vector<int> list1;
    vector<int> list2;
    map<string, int> dict1;
    map<string, int> dict2;
    string str1;
    string str2;
    int int1;
    int int2;
    float float1;
    float float2;
    char char1;
    char char2;

    function4(string name, int age, string gender, int income){
        this->name = name;
        this->age = age;
        this->gender = gender;
        this->income = income;
    }

    int calculate_final_value(){
        int final_value = this->int1 + this->int2 + float(this->float1) + float(this->float2) + this->list1.size() + this->list2.size() + this->dict1.size() + this->dict2.size() + this->str1.size() + this->str2.size() + int(this->char1) + int(this->char2);
        return final_value;
    }
};