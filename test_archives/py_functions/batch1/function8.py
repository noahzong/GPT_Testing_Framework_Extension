def function8(string1, int1, list1, boolean1):
  result = ""
  if boolean1:
    result = result + string1
  for i in list1:
    result = result + str(i)
  result = result + str(int1)
  return result