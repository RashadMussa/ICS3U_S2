items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []

# Predict A:
# Purpose: For each item in 'items', calculate its length (an integer) and append it to 'sizes'.
# Data types: items[i] is a string; sizeI is an int; sizes is a list of ints.
# Output: None here, just building the sizes list.

for i in range(len(items)):
    sizeI = len(items[i])
    sizes.append(sizeI)

# Predict B:
# Output will print the length followed by the item string for each index.
# Expected output:
# 6 Apples
# 7 Bananas
# 8 Cherries
# 4 Dosa

for i in range(len(sizes)):
    print("%d %s" % (sizes[i], items[i]))

# --- Modify: add a loop to check if sizes[i] matches length of items[i] string ---

for i in range(len(items)):
    match = (sizes[i] == len(items[i]))
    print("Index %d: size matches length? %s" % (i, match))
