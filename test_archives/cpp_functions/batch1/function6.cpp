int function6(int userInteger, string userString, vector<string> userList) {
  // Initialize variables
  int totalSum = 0;
  int wordCount = 0;
  int maxWordLength = 0;

  // Calculate the sum of the user input integer
  totalSum += userInteger;

  // Count the words in the user input string
  wordCount = std::count(userString.begin(), userString.end(), ' ') + 1;

  // Find the maximum word length in the user input list
  for (string word : userList) {
    if (word.length() > maxWordLength) {
      maxWordLength = word.length();
    }
  }

  // Return the sum of the total, word count and maximum word length
  return totalSum + wordCount + maxWordLength;
}