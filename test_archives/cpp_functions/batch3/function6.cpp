#include <iostream>
#include <string>
using namespace std;

string function6(string name, int age, bool likes_pizza, bool active_member) {
  string final_value = name + " is " + to_string(age) + " years old. ";
  if (likes_pizza == true) {
    final_value += "They like pizza. ";
  } 
  else {
    final_value += "They don't like pizza. ";
  }
  if (active_member == true) {
    final_value += "They are an active member.";
  } 
  else {
    final_value += "They are not an active member.";
  }
  return final_value;
}