#include <string>
#include <cmath>

using namespace std;

int function2(string string1, int int1, float float1){
  string1 = to_string(string1);
  int1 = static_cast<int>(int1);
  float1 = static_cast<float>(float1);

  float result = string1.length() * int1 * float1;
  return static_cast<int>(result);
}