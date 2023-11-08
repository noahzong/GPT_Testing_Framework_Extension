#include <iostream>
#include <string>

using namespace std;

int function8(int num1, string str1, bool bool1, int num2) {
    if (bool1) {
        return num1 + num2;
    } else {
        return str1.length();
    }
}