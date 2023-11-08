def function4 (num1, num2, num3, string1, list1): 
  '''
  Function4 takes 5 inputs: two numbers, 1 string, and a list.
  It adds together the numbers, concatenates the string,
  and sums all the elements of the list.
  It returns the final sum.
  '''
  return num1 + num2 + num3 + sum(list1) + len(string1)