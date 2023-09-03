def branch79(x,y):
  if x > 0 and y > 0:
    return x * y
  elif x < 0 and y < 0:
    return x + y
  elif x == 0:
    return 2 * y
  elif y == 0:
    return 3 * x
  else:
    return x - y