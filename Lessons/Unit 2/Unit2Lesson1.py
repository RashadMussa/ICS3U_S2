# Unit 2 - Lesson 1

# --- Prediction Task ---
# Predict: The code will output "I prefer cherries" if input is "C"
# Reflection: My prediction was correct. However, when we enter any input other than "A" or "B",
# the program still outputs "I prefer cherries". This is a problem because it incorrectly assumes
# all other input means "cherries", instead of only responding to "C".

# --- Modified Input Menu with Proper Branching ---
print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
elif (ch == "C"):
    print("I prefer cherries")
else:
    print("Invalid input. Please enter A, B, or C.")

# --- Marking System with Compound Conditionals ---
x = int(input("Enter a number between 1 and 100: "))

if (x >= 80) and (x <= 100):
    print("A")
elif (x >= 70) and (x <= 79):
    print("B")
elif (x >= 60) and (x <= 69):
    print("C")
elif (x >= 50) and (x <= 59):
    print("D")
elif (x >= 0) and (x < 50):
    print("F")
else:
    print("Not a valid number. Enter a number from 1 to 100.")
