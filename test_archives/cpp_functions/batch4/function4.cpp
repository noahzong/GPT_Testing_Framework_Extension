# C++ Code 
#include <iostream>
#include <string>
#include <list>

using namespace std;

string function4(int num1, string str1, list<int> list1) {
  int total = 0;
  for (int i : list1) {
    total += (num1 * i);
  }
  return to_string(total) + str1;
}