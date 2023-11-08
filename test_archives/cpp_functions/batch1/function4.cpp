// Declare and initialize variables
string str1 = "Hello World!";
int int1 = 3;
float float1 = 5.0;
int list1[] = {1,2,3};
map<int, string> dict1 = {{1,'a'}, {2,'b'}, {3,'c'}};

// Perform operations
int result1 = param1 + param2 + param3;
string result2 = str1 + " " + std::to_string(int1);
float result3 = float1 + list1[2];
string result4 = dict1[(int)result3 % 3];

// Return the final value
return result4;