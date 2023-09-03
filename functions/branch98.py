def branch98(input1, input2):
  if input1 > 0 and input2 > 0:
    result = input1 + input2
  elif input1 > 0 and input2 < 0:
    result = input1 - abs(input2)
  elif input1 < 0 and input2 > 0:
    result = abs(input1) + input2
  elif input1 < 0 and input2 < 0:
    result = abs(input1) - abs(input2)
  else:
    result = 0
  
  return result