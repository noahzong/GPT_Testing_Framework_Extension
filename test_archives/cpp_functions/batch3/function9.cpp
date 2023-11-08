#include <iostream>
#include <string>
#include <vector>

using namespace std;

string function9(string string, int int1, int int2, int int3, vector<int> list1) {
  int total = 0;
  for (int i : list1) {
    total += (i + int1 + int2 + int3);
  }
  
  return string + to_string(total);
}