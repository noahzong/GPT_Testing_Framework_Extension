# C++ Code
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class function6 {
public:
    int num1;
    int num2;
    string str1;
    string str2;
    vector<int> lst1;
    vector<int> lst2;

    function6(int num1, int num2, string str1, string str2, vector<int> lst1, vector<int> lst2) {
        this->num1 = num1;
        this->num2 = num2;
        this->str1 = str1;
        this->str2 = str2;
        this->lst1 = lst1;
        this->lst2 = lst2;
    }

    int get_sum() {
        return num1 + num2;
    }

    string get_concat() {
        return str1 + str2;
    }

    double get_lst_avg() {
        int lst_sum = 0;
        for (int val : lst1) {
            lst_sum += val;
        }
        for (int val : lst2) {
            lst_sum += val;
        }
        return lst_sum / (lst1.size() + lst2.size());
    }
};