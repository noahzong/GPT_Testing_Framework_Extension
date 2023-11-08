#include <string> 
#include <iostream>
using namespace std;

float function3(string string1, string string2, float float1, int int1) {
  float result = float1 + int1;
  result = result * stoi(string1);
  result = result / stoi(string2);
  return result;
}