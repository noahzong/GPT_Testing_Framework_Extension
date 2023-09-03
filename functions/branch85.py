def branch85(x, y):
  if x == 0:
    if y == 0:
      return 0
    elif y > 0:
      return 1
    else:
      return -1
  elif x > 0:
    if y == 0:
      return 2
    elif y > 0:
      return 3
    else:
      return 4
  else:
    if y == 0:
      return 5
    elif y > 0:
      return 6
    else:
      return 7