#include <string>
#include <iostream>

using namespace std;

float function9(string string1, string string2, int number1, float number2) {
    return number1 + number2 + string1.length() + string2.length();
}