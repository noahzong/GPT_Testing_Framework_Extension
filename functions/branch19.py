def branch19(x, y, z):
  if x == 0:
    if y == 0:
      return True
    else:
      return False
  else:
    if z == 0:
      return False
    else:
      if x > 0:
        return x + y - z
      else:
        return x - y + z