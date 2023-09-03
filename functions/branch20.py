def branch20(x, y, z):
  # If statements to define branch points
  if x == 0:
    if y == 0:
      if z == 0:
        result = 0
      else:
        result = 1
    else:
      result = 2
  else:
    if y == 0:
      if z == 0:
        result = 3
      else:
        result = 4
    else:
      result = 5
  
  # Return the result of the branching
  return result