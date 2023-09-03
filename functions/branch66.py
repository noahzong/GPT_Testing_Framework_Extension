def branch66(number, word):
  if number > 0 and word == 'yes':
    return 'positive'
  elif number > 0 and word == 'no':
    return 'positive but negative'
  elif number < 0 and word == 'yes':
    return 'negative but positive'
  elif number < 0 and word == 'no':
    return 'negative'
  else:
    return 'invalid input'