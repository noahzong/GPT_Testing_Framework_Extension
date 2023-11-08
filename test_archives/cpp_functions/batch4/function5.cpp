#include <iostream>
#include <string>
using namespace std;

string function5(string str1, string str2, int int1, int int2, float float1, float float2, bool bool1) {
  string final_value = str1[0] + str2[str2.length()-1] + to_string(int1*int2) + to_string(float1/float2) + to_string(bool1);
  return final_value;
}