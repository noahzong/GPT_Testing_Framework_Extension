#include <string>

std::string function7(std::string string, int int1, int int2, bool boolean){
  int final = 0;
  if(boolean == true){
    final = int1 + int2;
  } else {
    final = int1 * int2;
  }
  return string + " " + std::to_string(final);
}