def branch45(x,y):
  if x > y:
    result1 = x + y
  elif x < y:
    result1 = x * y
  else:
    result1 = x ** y

  if result1 > 10:
    result2 = result1 - 10
  elif result1 < 10:
    result2 = result1 + 10
  else:
    result2 = result1 * 10

  if result2 % 2 == 0:
    result3 = result2 / 2
  else:
    result3 = result2 * 2

  return result3