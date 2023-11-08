def function0(int_val, float_val, str_val, bool_val):
  total = 0
  if bool_val == True:
    total += int_val
  if str_val == 'hello':
    total += float_val
  
  return total