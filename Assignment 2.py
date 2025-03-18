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
target_number = random.randint(1, 100)  
# Randomly generate a number between 1 and 100 and assign it to 'target_number'

guess_count = 0  
# Set the initial guess count to 0 to track how many guesses the user has made

# Print introduction to the game
print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is.")
print("You have a maximum of six (6) tries.")

# Loop for user guesses
while guess_count < 6:
    guess_count += 1  
    # Increment the guess count by 1 with each iteration

    user_guess = int(input("Guess #%d: " % guess_count))  
    # Prompt the user to input their guess and convert it to an integer

    # Check if the guess is correct, too high, or too low
    if user_guess > target_number:
        print("Lower")  
        # If the guess is too high, prompt the user to guess a lower number
    elif user_guess < target_number:
        print("Higher!")  
        # If the guess is too low, prompt the user to guess a higher number
    else:
        print("You guessed right!")  
        # If the guess is correct, notify the user they won
        guess_count = 7  
        # End the game early by setting guess_count to 7

# After the loop ends, check if the user failed to guess the number
if user_guess != target_number:
    print("Sorry: you are out of guesses! The answer was %d. Better luck next time!" % target_number)
    # If the guess is still wrong after 6 attempts, inform the user and show the correct number
