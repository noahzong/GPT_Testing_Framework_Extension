def branch78(number1, number2):
  '''This function takes two inputs and outputs a value based on four branches'''
  if number1 > number2:
    return number1 + 10
  elif number1 == number2:
    return number1 * number2
  elif number1 < 0 and number2 < 0:
    return number1 + number2
  else:
    return number1 - number2