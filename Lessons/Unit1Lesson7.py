# Predict
# A) I predict that the output will say Yes y is a factor of x
# B) I predict that the output will be stuck at Now deciding if", y, "is a factor of", x, "..." because x isn't a factor of y

# Inspect
# Yes

# Modify

import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
rem = 0
if (y != 0):
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)

# Modify 2
import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
if(y != 0):
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)
else:
    print("You cannot divide by a non-zer number")

# Modify 3
import math

x = input(" Input a whole number between 1 and 20: ")
x = int(x) 
if ((x < 1 or x > 20)):
    print("The number must be between 1 and 20. Try again.")
else:
    y = input(" Input another nonzero whole number between 1 and 20:")
    y = int(y) 
    if ((y < 1 or y > 20)): 
        print("The number must be between 1 and 20.")
    else:
      print("Now deciding if", y, "is a factor of", x, "...")
      if y != 0:  
            rem = x % y
            if rem == 0:
                print("Yes!", y, "is a factor of", x)
            else:
                print("No,", y, "is not a factor of", x, "...")
