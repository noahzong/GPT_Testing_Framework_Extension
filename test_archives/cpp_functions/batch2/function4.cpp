int function4(int num1, int num2, int num3, string string1, vector<int> list1) {
  int result = num1 + num2 + num3;
  int list1Sum = 0;
  for (int i = 0; i < list1.size(); i++) {
    list1Sum += list1[i];
  }
  result += list1Sum + string1.length();
  return result;
}