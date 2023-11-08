int function2(int num1, int num2, string str1, vector<string> list1, bool bool1) {
  int result = 0;
  if (bool1 == true) {
    result = num1 + num2;
  }
  else {
    result = num1 - num2;
  }
  for (int i = 0; i < list1.size(); i++) {
    result += str1.length(); 
  }
  return result;
}