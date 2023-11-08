int function0(int int_val, float float_val, string str_val, bool bool_val) {
  int total = 0;
  if (bool_val == true) {
    total += int_val;
  }
  if (str_val == "hello") {
    total += float_val;
  }
  return total;
}