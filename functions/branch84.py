def branch84(num1, num2, str1):
  if str1 == "A":
    if num1 > num2:
      return num1 + num2
    elif num1 < num2:
      return num1 * num2
    else:
      return num1 ** num2
  elif str1 == "B":
    if num1 > num2:
      return num1 - num2
    elif num1 < num2:
      return num2 - num1
    else:
      return num1 / num2
  else:
    if num1 > num2:
      return num1 % num2
    elif num1 < num2:
      return num2 % num1
    else:
      return num1 + num2 + 3