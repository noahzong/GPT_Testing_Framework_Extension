def function9(string, int1, int2, int3, list1):
  total = 0
  for i in list1:
    total += (i + int1 + int2 + int3)
  
  return string + str(total)