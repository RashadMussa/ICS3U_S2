# Define the add function
def add(a: float, b: float) -> float:
    sum = a + b
    return sum

# Predict and test add(7, 2)
print(add(7, 2))  # Expected output: 9 (int)

# Modify 1
sum_val = add(7.0, 2.0)
print(sum_val)  # Expected output: 9.0 (float)
print("Type of sum_val:", type(sum_val))

# What happens with strings "7" and "2"
sum_str = add("7", "2")
print(sum_str)  # Expected output: "72" (string concatenation)
print("Is sum_str a string?", isinstance(sum_str, str))

# What happens with strings "book" and "keeper"
sum_words = add("book", "keeper")
print(sum_words)  # Expected output: "bookkeeper" (string concatenation)
print("Is sum_words a string?", isinstance(sum_words, str))

# Modify 2: Define the myAbs function
def myAbs(n):
    if n < 0:
        return -n
    else:
        return n

b = -12
a = myAbs(b)
print("The absolute value of %d is %d" % (b, a))
