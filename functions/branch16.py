def branch16(in_1, in_2, in_3):
  # first branch
  if in_1 == 1:
    out_1 = in_2 + in_3
  elif in_1 == 2:
    out_1 = in_2 - in_3
  elif in_1 == 3:
    out_1 = in_2 * in_3
  else:
    out_1 = in_2 / in_3
  
  # second branch
  if out_1 > 0:
    out_2 = out_1 + in_1
  elif out_1 < 0:
    out_2 = out_1 - in_1
  else:
    out_2 = out_1 * in_1
  
  # third branch
  if out_2 > 0 and in_3 > 0:
    out_3 = out_2 * in_3
  elif out_2 < 0 and in_3 < 0:
    out_3 = out_2 / in_3
  else:
    out_3 = out_2 + in_3
  
  # fourth branch
  if out_3 > 0:
    out_4 = out_3 + in_1
  elif out_3 < 0:
    out_4 = out_3 - in_1
  else:
    out_4 = out_3 * in_1
  
  return out_4