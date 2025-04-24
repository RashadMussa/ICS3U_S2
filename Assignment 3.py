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
# Display intro message
print("Palindrome program!")

# Define a list of 10 words to check
word_list = ["level", "noon", "goal", "radar", "bed", "soccer", "civic", "hotel", "cake", "madam"]

# Loop through each word in the list
for current_word in word_list:
    match_count = 0
    index = 0
    mid_point = len(current_word) // 2

    # Loop to compare characters from front and back
    while index < mid_point:
        front_char = current_word[index]
        back_char = current_word[len(current_word) - 1 - index]

        if front_char == back_char:
            match_count += 1
            index += 1
        else:
            # Exit loop by forcing index to mid_point 
            index = mid_point
            print(current_word, "is not a palindrome")

        if match_count == mid_point:
            print(current_word, "is a palindrome")

# End of program message
print("Goodbye!")
