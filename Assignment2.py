# Student Name: [Your Name]
# Student Number: [Your Student Number]
# Course Code: [Your Course Code]
# Variable Dictionary:
#   target_number: The randomly generated number the user is trying to guess (int).
#   guess_count: The number of guesses the user has made (int).
#   user_guess: The number guessed by the user (int).
#   max_guesses: The maximum number of guesses allowed (int).

import random

# Initialize the game
target_number = random.randint(1, 100)  # Randomly generate a number between 1 and 100
guess_count = 0  # Track the number of guesses
max_guesses = 6  # Maximum number of guesses allowed

print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is.")
print("You have a maximum of six (6) tries.")

# Loop for user guesses
while guess_count < max_guesses:
    guess_count += 1
    print("Guess #", end="")
    print(guess_count, end="")
    print(": ", end="")
    
    try:
        user_guess = int(input())  # Get user's guess
    except ValueError:
        print("Please enter a valid number between 1 and 100.")
        guess_count -= 1  # Reset guess count if input is invalid
        continue

    # Check if the guess is correct, too high, or too low
    if user_guess == target_number:
        print("You guessed right!")
        break  # End the game if the guess is correct
    elif user_guess < target_number:
        print("Higher!")
    else:
        print("Lower!")

# If the user runs out of guesses
if guess_count == max_guesses:
    print("Sorry: you are out of guesses! The answer was ", end="")
    print(target_number, end="")
    print(". Better luck next time!")
