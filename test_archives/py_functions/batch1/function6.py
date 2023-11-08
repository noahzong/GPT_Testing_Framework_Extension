def function6(userInteger, userString, userList):
  # Initialize variables
  totalSum = 0
  wordCount = 0
  maxWordLength = 0

  # Calculate the sum of the user input integer
  totalSum += userInteger

  # Count the words in the user input string
  wordCount = len(userString.split())

  # Find the maximum word length in the user input list
  for word in userList:
    if len(word) > maxWordLength:
      maxWordLength = len(word)

  # Return the sum of the total, word count and maximum word length
  return totalSum + wordCount + maxWordLength