def branch53(num1, num2, char):
  if num1 > 0 and num2 < 0:
    if char == 'a':
      return num1 + num2
    elif char == 'b':
      return num1 - num2
    elif char == 'c':
      return num1 * num2
    else:
      return 'error'
  elif num1 < 0 and num2 > 0:
    if char == 'a':
      return num2 - num1
    elif char == 'b':
      return num1 + num2
    elif char == 'c':
      return num1 / num2
    else:
      return 'error'
  else:
    if char == 'a':
      return num1 * num2
    elif char == 'b':
      return num1 / num2
    elif char == 'c':
      return num1 + num2
    else:
      return 'error'