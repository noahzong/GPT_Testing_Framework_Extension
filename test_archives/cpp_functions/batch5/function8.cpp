#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include <map>
using namespace std;

class function8 {
public:
    int x;
    int y;
    int z;
    string str_var;
    int int_var;
    float float_var;
    bool bool_var;
    vector<int> list_var;
    tuple<int, int> tuple_var;
    map<int, int> dict_var;

    function8(int x, int y, int z) {
        this->x = x;
        this->y = y;
        this->z = z;
        this->str_var = "variable";
        this->int_var = 0;
        this->float_var = 0.0;
        this->bool_var = false;
        this->list_var = {};
        this->tuple_var = {};
        this->dict_var = {};
    }

    string combine_vars() {
        return this->str_var + to_string(this->int_var) + to_string(this->float_var) + to_string(this->bool_var) + to_string(this->list_var) + to_string(this->tuple_var) + to_string(this->dict_var) + to_string(this->x) + to_string(this->y) + to_string(this->z); 
    }

};