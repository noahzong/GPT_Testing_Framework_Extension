def branch47(x, y, z):
  if (x == 0):
    result = y + z
  elif (x > 0 and y == 0):
    result = x - z
  elif (x < 0 and y < 0):
    result = x * z
  elif (x > 0 and y > 0):
    if (z == 0):
      result = x / y
    else:
      result = x + y + z
  else:
    result = "Invalid input"
  return result