import math

# Header
print("  N|  SQR|  Cubes|Roots")
print("---+-----+-------+-----")

for n in range(10, 201, 15):
    n2 = n ** 2
    n3 = n ** 3
    root = math.sqrt(n)
    print("%3d|%5d|%7d|%5.2f" % (n, n2, n3, root))
