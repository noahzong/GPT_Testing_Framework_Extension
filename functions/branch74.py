def branch74(x,y):
  if x > y:
    z = x - y
    if z < 5:
      return z
    else:
      z = z * 2
      if z > 10:
        return z
      else:
        z = z + 5
        if z % 2 == 0:
          return z
        else:
          z = z + 1
          return z
  else:
    z = y - x
    if z < 5:
      return z
    else:
      z = z * 3
      if z > 10:
        return z
      else:
        z = z + 4
        if z % 2 == 0:
          return z
        else:
          z = z + 2
          return z