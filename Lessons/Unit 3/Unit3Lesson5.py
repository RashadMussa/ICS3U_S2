myList = [22, 16, 59, 67, 55, 84, 7, 91, 89, 48, 69, 30, 98, 28, 31]

# Initialize highest and smallest to the first element
highest = myList[0]
smallest = myList[0]
total_sum = 0

# Loop through each number in the list
for number in myList:
    # Update highest if current number is greater
    if number > highest:
        highest = number
    
    # Update smallest if current number is smaller
    if number < smallest:
        smallest = number
    
    # Add current number to total sum
    total_sum += number

# Print results
print("The largest number is:", highest)
print("The smallest number is:", smallest)
print("The sum is:", total_sum)
