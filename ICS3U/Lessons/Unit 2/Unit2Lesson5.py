# Unit 2 - Lesson 5: Counted Loops and Making Shapes

# Predict:
# This will print a right-angle triangle of increasing '#' characters
S = "#"
for i in range(1, 11):
    print(S * i)

# Output:
# #
# ##
# ###
# ####
# #####
# ######
# #######
# ########
# #########
# ##########

# Try this:
# Repeating "--8<--" 10 times
pattern = "--8<--"
print(pattern * 10)

# Modify 1:
# Predict the output for range(-5, 5)
# Output: -5, -4, -3, -2, -1, 0, 1, 2, 3, 4
for i in range(-5, 5):
    print(i, end=" ")
print()

# Try this: reversed triangle using a for loop
for i in range(10, 0, -1):
    print("#" * i)

# Modify 2: Centered triangle
rows = 5
for i in range(rows):
    spaces = rows - i - 1
    hashes = 2 * i + 1
    print(" " * spaces + "#" * hashes)

# Modify 3: Diamond shape
rows = 5

# Upper half
for i in range(rows):
    spaces = rows - i - 1
    hashes = 2 * i + 1
    print(" " * spaces + "#" * hashes)

# Lower half
for i in range(rows - 2, -1, -1):
    spaces = rows - i - 1
    hashes = 2 * i + 1
    print(" " * spaces + "#" * hashes)
