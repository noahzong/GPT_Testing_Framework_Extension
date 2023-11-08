int function9(int int1, float float1, string str1, vector<int> list1) {
  int total = int1 + float1 + str1.length();
  
  for (int i : list1) {
    total += i;
  }
  
  return total;
}