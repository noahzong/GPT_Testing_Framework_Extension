def function2(string1, int1, float1):
  '''
  This function takes three data types as parameters: a string, an integer, and a float.
  It returns a single integer value.
  '''
  string1 = str(string1)
  int1 = int(int1)
  float1 = float(float1)
  
  result = len(string1) * int1 * float1
  return int(result)