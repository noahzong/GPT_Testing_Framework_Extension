from functions.branch77 import branch77
def test_branch77():
   # Test when x is 1
   assert branch77(1,2,3) == "x, y, and z are all equal to 1, 2, and 3!"
   assert branch77(1,2,4) == "x and y are equal to 1 and 2, and z is greater than 3!"
   assert branch77(1,2,1) == "x and y are equal to 1 and 2, and z is less than 3!"
   
   # Test when x is greater than 1
   assert branch77(3,2,3) == "x is greater than 1, y is equal to 2, and z is equal to 3!"
   assert branch77(3,2,4) == "x is greater than 1, y is equal to 2, and z is greater than 3!"
   assert branch77(3,2,1) == "x is greater than 1, y is equal to 2, and z is less than 3!"
   
   # Test when x is less than 1
   assert branch77(0,2,3) == "x is less than 1, y is equal to 2, and z is equal to 3!"
   assert branch77(0,2,4) == "x is less than 1, y is equal to 2, and z is greater than 3!"
   assert branch77(0,2,1) == "x is less than 1, y is equal to 2, and z is less than 3!"