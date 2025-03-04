import random  # Import the random module to generate a random number

# Simple Number Guessing Game

def number_guessing_game():
    print("Welcome to the number guessing game!")  # Print game introduction
    print("Guess a number between 1 and 100. You have 6 tries.")  # Explain the rules
    
    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    
    attempt = 1  # Initialize the attempt counter
    while attempt <= 6:  # Loop until the user has used all 6 attempts
        print("Guess #", attempt, ": ", end="")  # Prompt the user for a guess
        guess = int(input())  # Read user input and convert it to an integer
        
        if guess < secret_number:  # Check if the guess is too low
            print("Higher!")  # Tell the user to guess higher
        elif guess > secret_number:  # Check if the guess is too high
            print("Lower!")  # Tell the user to guess lower
        else:  # If the guess is correct
            print("You guessed right!")  # Congratulate the user
            return  # End the game
        
        attempt += 1  # Increment the attempt counter
    
    print("Out of guesses! The number was", secret_number, ".")  # Reveal the correct number if the user fails

number_guessing_game()  # Start the game
