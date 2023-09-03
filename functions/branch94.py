def branch94(x, y, z):
  if x > y and x > z:
    return x
  elif y > x and y > z:
    return y
  elif z > x and z > y:
    return z
  elif x == y and x > z:
    return x + y
  elif x == z and x > y:
    return x + z
  elif y == z and y > x:
    return y + z
  elif x == y == z:
    return x + y + z
  else:
    return None