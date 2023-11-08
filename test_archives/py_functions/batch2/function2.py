def function2(num1, num2, str1, list1, bool1): 
  ''' 
  This function takes in multiple data types and variables 
  :param num1: Number 
  :param num2: Number 
  :param str1: String 
  :param list1: List 
  :param bool1: Boolean 
  :return: Number 
  '''
  result = 0
  if bool1 == True: 
    result = num1 + num2 
  else: 
    result = num1 - num2 
  for item in list1: 
    result += len(str1) 
  
  return result