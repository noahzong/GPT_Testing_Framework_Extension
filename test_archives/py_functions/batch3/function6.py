def function6(name, age, likes_pizza, active_member):
  final_value = name + " is " + str(age) + " years old. "
  if likes_pizza == True:
    final_value += "They like pizza. "
  else:
    final_value += "They don't like pizza. "
  if active_member == True:
    final_value += "They are an active member."
  else:
    final_value += "They are not an active member."
  return final_value