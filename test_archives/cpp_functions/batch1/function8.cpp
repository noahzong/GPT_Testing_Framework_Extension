#include <iostream>
#include <string>
#include <vector>

using namespace std;

string function8(string string1, int int1, vector<int> list1, bool boolean1) {
  string result = "";
  if (boolean1) {
    result = result + string1;
  }
  for (int i : list1) {
    result = result + to_string(i);
  }
  result = result + to_string(int1);
  return result;
}

int main() {
  string string1 = "Hello";
  int int1 = 5;
  vector<int> list1 = {1,2,3,4};
  bool boolean1 = true;
  cout << function8(string1, int1, list1, boolean1);
  return 0;
}