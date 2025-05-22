# Original string
progname = "Python"

# Prediction A: print(progname) will print "Python"
print(progname)  # Python

# Prediction B: print(progname[0]) will print 'P' (the first character)
print(progname[0])  # P

# Prediction C: This loop prints each character in the string without newline or spaces
for c in progname:
    print(c, sep="", end="")  # Output: Python (all characters on the same line)
print()  # E: This empty print adds a newline after the loop

# Prediction F: This loop prints the index and corresponding character
for c in range(len(progname)):
    print(c, progname[c])
# Output:
# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n

# Reflection D:
# Setting sep="" (separator) doesn't affect this print because only one item is printed each time.
# Setting end="" means no newline is added after each print, so characters print on the same line.

# Reflection E:
# The empty print() adds a newline so that subsequent prints start on a new line.

# --- Modify ---

# Using dummy text from lipsum.com
progname = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis in."

# Count spaces in the string
space_count = 0
for char in progname:
    if char == " ":
        space_count += 1

print("There are %d spaces in the text." % space_count)
# Suggested output example: There are 9 spaces in the text.
