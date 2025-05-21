ar2 = [
    [3, 4, 1, 2, 6],
    [9, 2, 3, 7, 5],
    [4, 2, 1, 0, 3]
]

# Predict A:
# This nested loop prints each element in each sub-array separated by spaces,
# with a newline after each row.
# Expected output:
# 3 4 1 2 6 
# 9 2 3 7 5 
# 4 2 1 0 3 

for i in range(len(ar2)):
    ar3 = ar2[i]
    for j in range(len(ar3)):
        print(ar3[j], end=" ")
    print()  # end of row

# Predict B:
# Printing ar2 directly prints the list of lists representation:
# [[3, 4, 1, 2, 6], [9, 2, 3, 7, 5], [4, 2, 1, 0, 3]]

print(ar2)

# --- Modify: Compute sums of each row and store in a new 3x1 array (list) ---

row_sums = []
for row in ar2:
    total = 0
    for num in row:
        total += num
    row_sums.append(total)

# Print the sums as comma-separated values in one line
print(", ".join(str(x) for x in row_sums))
