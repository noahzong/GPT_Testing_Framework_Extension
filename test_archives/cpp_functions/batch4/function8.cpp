# C++ code:
#include<iostream>
#include<string>
#include<vector>

using namespace std;

pair<string, vector<int>> function8(int int1, int int2, string str1, vector<int> list1) {
    vector<int> new_list;
    for (int i : list1) {
        new_list.push_back(i + int1);
    }
    int final_int = int2 * int1;
    string final_str = str1 + to_string(final_int);
    return {final_str, new_list};
}

int main() {
    int int1 = 3;
    int int2 = 5;
    string str1 = "The answer is ";
    vector<int> list1 = {1,2,3};

    auto result = function8(int1, int2, str1, list1);
    cout << result.first << " ";
    for (int i : result.second) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}