"""
Author : Rashad Mussa
Student Number: 762918
Due date : 28 Feburary 2025
"""

"""
Part 1
Program : Even Odd Predictor
Description : Predit if calculation will produce an even or odd number.
VARIABLE DICTIONARY :
first_number (int) = Stores the first positive whole number input by the user.
second_number (int) = Stores the second positive whole number input by the user.
"""
print("Welcome to the Even and Odd Product Detector!")
print("This tool helps you determine whether the product of two positive whole numbers is even or odd.")

# Prompt the user to input two numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Determine if the product is even or odd based on the input numbers
if first_number % 2 == 1 and second_number % 2 == 1:
    # Both numbers are odd
    print("The product of", first_number, "*", second_number, "will be odd.")
elif first_number % 2 == 0 and second_number % 2 == 0:
    # Both numbers are even
    print("The product of", first_number, "*", second_number, "will be even.")
else:
    # One number is even, and the other is odd
    print("The product of", first_number, "*", second_number, "will be even.")
"""
Part 2
Program : Cube Inner Diagonal Calculator
Description : Calculates the inner diagonal of a cube based on its edge length.
VARIABLE DICTIONARY :
edge_length	(int)	= Stores the length of the cube's edge input by the user.
diagonal (float) = Stores the calculated inner diagonal of the cube, rounded to 2 decimal places.
"""
import math

print("I will find the cube's inner diagonal for any edge length!")
# Describes the purpose of the program

edge_length = int(input("Please enter the edge length of your cube: "))
# Prompts the user to input the edge length of the cube

diagonal = edge_length * math.sqrt(3)
# Calculates the inner diagonal using the formula: edge_length * √3

diagonal = round(diagonal, 2)
# Rounds the diagonal value to 2 decimal places

print("The length of the inner diagonal of a cube with side length %.f is: %.2f" % (edge_length, diagonal))
# Displays the result with the edge length and rounded diagonal

"""
Part 3
Program : Change calculator
Description : Calculates the breakdown of coins (quarters, dimes, nickels, pennies) for a given amount of cents, excluding dollar amounts.
VARIABLE DICTIONARY :
cents (int) = Stores the amount of money in cents input by the user.
quarters (int) = Stores the number of quarters calculated from the remaining cents.
remaining (int) = Tracks the leftover cents after each coin calculation.
dimes (int) = Stores the number of dimes calculated from the remaining cents.
nickels	(int) = Stores the number of nickels calculated from the remaining cents.
pennies	(int) = Stores the number of pennies calculated from the remaining cents.
"""
# Coin Change Calculator
cents = int(input("Enter the amount of money in cents: "))  # Prompts user to input cents

print("Calculating coin breakdown...")  # Informs user that the program is processing

if cents >= 100:  # Checks if the amount is a dollar or more
    cents = cents % 100  # Removes the dollar amount, keeping only cents

# Calculate the number of each coin
quarters = cents // 25  # Number of quarters
remaining = cents % 25   # Remaining cents after quarters

dimes = remaining // 10  # Number of dimes
remaining = remaining % 10  # Remaining cents after dimes

nickels = remaining // 5  # Number of nickels
pennies = remaining % 5   # Number of pennies

# Display the results, skipping coins with zero count
if quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("You have one dollar.")  # Special case for exactly 100 cents
else:
    print(f"{cents} cents can be broken down into:")
    if quarters > 0:
        print(f"{quarters} quarters")
    if dimes > 0:
        print(f"{dimes} dimes")
    if nickels > 0:
        print(f"{nickels} nickels")
    if pennies > 0:
        print(f"{pennies} pennies")













