birth_year = int(input("Please enter your year of birth: "))
age = int(input("Please enter your age: "))
result = birth_year * 2 + 5
result = result * 50 + age
result = (result - 250) / 100
print("Your birth year with the decimal of your age is", result)
