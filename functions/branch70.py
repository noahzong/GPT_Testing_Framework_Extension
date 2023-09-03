def branch70(num1, num2, num3):
  # Check if num1 is equal to num2
  if num1 == num2:
    # If num1 is greater than num3, return the sum
    if num1 > num3:
      return num1 + num2
    # If num1 is equal to num3, return their product
    elif num1 == num3:
      return num1 * num2
    # Otherwise, return num3
    else:
      return num3
  # If num1 is not equal to num2
  else:
    # If num1 is greater than num3, return the difference
    if num1 > num3:
      return num1 - num2
    # If num2 is greater than num3, return the sum
    elif num2 > num3:
      return num1 + num2
    # Otherwise, return num3
    else:
      return num3