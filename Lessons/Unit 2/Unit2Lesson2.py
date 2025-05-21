# Unit 2 - Lesson 2: Conditional Loops

# --- Part A ---
# Predict: I think the code will print number 9 all the way to number 1 in descending order.
# Reflection: Prediction was correct. It printed: 9, 8, ..., 1

count = 9
while (count != 0):
    print(count)
    count -= 1

# Modify 1:
# Predict: I think the code will print number 8 all the way to number 0 in descending order.
count = 9
while (count != 0):
    count -= 1
    print(count)

# --- Part B: Triangular Numbers ---
adder = 0
number = 0
position = "1st"

while adder < 6:
    adder += 1
    number += adder

    if adder == 1:
        suffix = "st"
    elif adder == 2:
        suffix = "nd"
    elif adder == 3:
        suffix = "rd"
    else:
        suffix = "th"

    print("The %d%s triangular number is %d" % (adder, suffix, number))
