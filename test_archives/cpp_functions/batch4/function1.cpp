# C++ Code
#include <string>
using namespace std;

int function1(string string1, int int1, bool bool1) {
  // Initialize total
  int total = 0;

  // Add string1 and int1 to total
  total += string1.length() + int1;

  // If boolean is true, add 10 to total
  if (bool1 == true) {
    total += 10;
  }

  // Return total
  return total;
}