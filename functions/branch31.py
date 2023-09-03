def branch31(a, b, c):
  if a == 0:
    return 0
  elif a == 1:
    if b == 0:
      return 1
    elif b == 1:
      if c == 0:
        return 2
      elif c == 1:
        return 3
  elif a == 2:
    if b == 0:
      if c == 0:
        return 4
      elif c == 1:
        return 5
    elif b == 1:
      return 6
  elif a == 3:
    if b == 0:
      if c == 0:
        return 7
      elif c == 1:
        return 8
    elif b == 1:
      if c == 0:
        return 9
      elif c == 1:
        return 10