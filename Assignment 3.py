"""
   Author : Rashad Mussa
   Student Number : 762918
   Revision Date : 23 April 2025
   Course Code : ICS3U
   Program : Is it a Palindrome?
   Description : A program that checks each word in a list to determine if it is a palindrome.
   VARIABLE DICTIONARY :
     word_list (list) = A list containing 10 words, some of which are palindromes
     word (string) = The current word being checked from the list
     letter_position (int) = Index used to compare characters from the start and end of the word
     matched_letters (int) = Number of matching character pairs in the word
     middle (int) = The halfway index of the current word
"""
# Start of the program
print("Palindrome program!")

# Define a list of 10 words (some palindromes, some not)
word_list = ["civic", "basketball", "radar", "goal", "kayak", "soccer", "racecar", "hotel", "refer", "loop"]

# Go through each word in the list
for word in word_list:
    letter_position = 0
    matched_letters = 0
    middle = len(word) // 2

    # Check each letter from the beginning and end of the word
    while letter_position < middle:
        if word[letter_position] == word[len(word) - 1 - letter_position]:
            matched_letters += 1
            letter_position += 1
        else:
            # Found a mismatch, so it's not a palindrome
            print(word, "is not a palindrome")
            # Exit the loop early without using break
            letter_position = middle

        # If all matched letters reach halfway, it's a palindrome
        if matched_letters == middle:
            print(word, "is a palindrome")

# End of program message
print("Goodbye!")
