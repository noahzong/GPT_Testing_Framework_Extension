def branch76(x, y, z):
  if x > 0 and y > 0 and z > 0:
    result = x + y + z
  elif x > 0 and y > 0 and z == 0:
    result = x * y
  elif x > 0 and y == 0 and z > 0:
    result = x + z
  elif x > 0 and y == 0 and z == 0:
    result = x
  elif x == 0 and y > 0 and z > 0:
    result = y * z
  elif x == 0 and y > 0 and z == 0:
    result = y
  elif x == 0 and y == 0 and z > 0:
    result = z
  else:
    result = 0
  return result