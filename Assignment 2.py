import random

# Initialize the game
target_number = random.randint(1, 100)  # Randomly generate a number between 1 and 100
guess_count = 0  # Track the number of guesses
max_guesses = 6  # Maximum number of guesses allowed
guessed_correctly = False  # Flag to track if the user has guessed the number

print("Hello! Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is.")
print("You have a maximum of six (6) tries.")

# Loop for user guesses
while guess_count < max_guesses and not guessed_correctly:
    guess_count += 1
    print("Guess #", guess_count, ": ", end="")

    user_guess = input()  # Get user's guess as a string

    # Directly attempt to convert the input to an integer
    if 1 <= int(user_guess) <= 100:
        user_guess = int(user_guess)

        # Check if the guess is correct, too high, or too low
        if user_guess == target_number:
            print("You guessed right!")
            guessed_correctly = True  # Set flag to True when the correct number is guessed
        elif user_guess < target_number:
            print("Higher!")
        else:
            print("Lower!")
    else:
        print("Please enter a number between 1 and 100.")
        guess_count -= 1  # Reset guess count if input is out of range

# If the user runs out of guesses or guesses correctly
if guessed_correctly:
    print("Congratulations! You guessed the number in", guess_count, "tries.")
else:
    print("Sorry: you are out of guesses! The answer was", target_number, ". Better luck next time!")
