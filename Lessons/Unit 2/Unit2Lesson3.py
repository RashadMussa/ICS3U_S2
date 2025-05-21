# Unit 2 - Lesson 3: Factorial Calculator

# Factorial Calculator:
# This program prints all factorials from 0! up to n!

print("Factorial Calculator:")
limiter = int(input("Enter a value for the upper limit, n: "))

limit = 0
factorialValue = 1

while limit <= limiter:
  if limit == 0:
    factorialValue = 1
  else:
    factorialValue = factorialValue * limit

  print("%d! factorial is %d" % (limit, factorialValue))
  limit += 1
