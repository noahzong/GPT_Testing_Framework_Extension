def branch62(input1, input2):
  #if-else statement
  if input1 > 0 and input2 > 0:
    output = input1 * input2
  elif input1 < 0 and input2 < 0:
    output = input1 + input2
  elif input1 > 0 and input2 < 0:
    output = input1 - input2
  else:
    output = input1 * 5
  
  #nested if-else statement
  if output >= 0:
    output2 = output + 10
  else:
    if input1 > input2:
      output2 = output - 10
    else:
      output2 = output + 20
  
  #return statement
  return output2