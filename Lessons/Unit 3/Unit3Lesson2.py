# Initial code given:

items = ["Apples", "Bananas", "Cherries", "Dosa"]

# Predict A: print(items) prints the list with brackets and quotes
print(items)  # Output: ['Apples', 'Bananas', 'Cherries', 'Dosa']

# Predict B: print number of items using len()
print("The number of items is %d." % len(items))  # Output: The number of items is 4.

# Predict C: loop through items and print each
for i in items:
    print(i)
# Output:
# Apples
# Bananas
# Cherries
# Dosa

# Predict D: loop through indexes and print index and item
for c in range(len(items)):
    print(c, items[c])
# Output:
# 0 Apples
# 1 Bananas
# 2 Cherries
# 3 Dosa


# --- Modify to accept user input ---

num_items = int(input("How many items are you entering? "))
print("Enter your items now:")

user_items = []
for _ in range(num_items):
    item = input("Next item: ")
    user_items.append(item)

print("You have entered %d items." % len(user_items))
for item in user_items:
    print(item)
