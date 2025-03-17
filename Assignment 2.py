"""
Author : Rashad Mussa
Student Number: 762918
Due date : 17 March 2025
"""

"""
Program : Number Guessing Game
Description : A game where the user tries to guess a randomly generated number between 1 and 100 within 6 tries.
VARIABLE DICTIONARY :
target_number (int) = Stores the randomly generated number between 1 and 100.
guess_count (int) = Tracks the number of guesses the user has made.
max_tries (int) = The maximum number of guesses allowed (6).
user_guess (int) = Stores the number input by the user on each guess.
"""


import random

# Initialize the game
target_number = random.randint(1, 100)  # Randomly generate a number between 1 and 100
guess_count = 0  # Track the number of guesses
print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is.")
print("You have a maximum of six (6) tries.")

# Loop for user guesses
while guess_count < 6:
    guess_count += 1
    user_guess = int(input("Guess #%d: " % guess_count))
    
    # Check if the guess is correct, too high, or too low
    if user_guess > target_number:
        print("Lower")
    elif user_guess < target_number:
        print("Higher!")
    else:
        print("You guessed right!")
        guess_count = 7

# After the loop ends, check if the user failed to guess the number
if user_guess != target_number:
    print("Sorry: you are out of guesses! The answer was %d. Better luck next time!" % target_number)
