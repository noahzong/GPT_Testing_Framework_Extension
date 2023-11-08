def function5(str1, str2, int1, int2, float1, float2, bool1):
  """This function takes in two strings, two integers, two floats, and a boolean,
  and returns one final value.
  """
  final_value = str1[0] + str2[-1] + str(int1*int2) + str(float1/float2) + str(bool1)
  return final_value