def branch13(x, y):
  if x == 0 and y == 0:
    return 0
  elif x == 0 or y == 0:
    return 1
  elif x > 0 and y > 0:
    return 2
  elif x < 0 and y < 0:
    return 3
  elif x > 0 and y < 0:
    return 4
  elif x < 0 and y > 0:
    return 5
  else:
    return 6