def branch58(num1, num2):
  if num1 > num2:
    return num1 + 10
  elif num2 > num1:
    return num2 - 10
  else:
    if num1 > 0:
      return num1 * num2
    elif num1 < 0:
      return num1 / num2
    else:
      if num2 > 0:
        return num1 + num2
      elif num2 < 0:
        return num1 - num2
      else:
        if num1 % 2 == 0:
          return num1 + (num2 * 2)
        else:
          return num1 - (num2 * 2)