int function5(int a, string b, float c, vector<int> d) {
  int result = a;
  result += b.length();
  result += c;
  result += d.size();
  return result;
}