def function9(int1, float1, str1, list1):
  # int1 is integer 
  # float1 is float
  # str1 is string
  # list1 is list
  
  total = int1 + float1 + len(str1)
  
  for i in list1:
    total += i
  
  return total