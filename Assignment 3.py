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
# Print a welcome message to indicate the start of the program  

# Define a list of 10 words to check  
word_list = ["level", "noon", "goal", "radar", "bed", "soccer", "civic", "hotel", "cake", "madam"]  
# Create a list of 10 words to be tested for being palindromes  

# Loop through each word in the list  
for current_word in word_list:  
# Iterate through each word in the word_list one by one  

    match_count = 0  
    # Initialize a counter to keep track of matching character pairs  

    index = 0  
    # Set the starting index for comparison to 0  

    mid_point = len(current_word) // 2  
    # Calculate the midpoint of the word (only need to compare up to this point)  

    # Loop to compare characters from front and back  
    while index < mid_point:  
    # Continue looping until all necessary characters have been compared  

        front_char = current_word[index]  
        # Get the character from the front of the word at the current index  

        back_char = current_word[len(current_word) - 1 - index]  
        # Get the character from the end of the word at the mirrored index  

        if front_char == back_char:  
        # Check if the characters from the front and back match  

            match_count += 1  
            # Increment match_count if the characters are equal  

            index += 1  
            # Move to the next character for comparison  

        else:  
        # If the characters do not match  

            # Exit loop by forcing index to mid_point   
            index = mid_point  
            # Set index to mid_point to break out of the loop  

            print(current_word, "is not a palindrome")  
            # Print that the word is not a palindrome  

        if match_count == mid_point:  
        # After all comparisons, if the number of matches equals mid_point  

            print(current_word, "is a palindrome")  
            # Print that the word is a palindrome  
            
            # End of program message
            print("Goodbye!")
