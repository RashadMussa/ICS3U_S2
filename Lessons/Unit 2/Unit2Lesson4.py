# Unit 2 - Lesson 4: Counted Loops with For Loops

print("Give me a value of n:")
n = int(input())

print("Counting from j = 1 to %d:" % n)
print("  j   tri       factorial")

triangular = 0
factorial = 1

for j in range(1, n + 1):
    triangular += j
    factorial *= j
    print("{:>4} {:>5} {:>12}".format(j, triangular, factorial))
