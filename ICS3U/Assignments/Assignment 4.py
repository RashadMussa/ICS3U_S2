"""
Author: Rashad Mussa
Course: ICS3U
Last Updated: May 19, 2025
Program: Wordle Finder
Description: This program lets the user search a Wordle solution file
either by entering a word or by entering a specific date.

VARIABLE DICTIONARY:
data_lines (list): stores each line from the file as [month, day, year, word]
dates (list): holds numeric dates converted to YYYYMMDD format
answers (list): contains Wordle solution words from the file
months (list): 3-letter month abbreviations used for conversion to numbers
file (file): file object used to read the data
line (str): temporarily holds each line read from the file
entry (list): a single line from the file split into components
mon (str): month part of the date (e.g. "Jan")
dy (str): day part of the date (e.g. "07")
yr (str): year part of the date (e.g. "2023")
user_word (str): the word entered by the user in word search
found (int): numeric date result from search_word()
target (int): numeric date built from user input in search_date()
result (str/None): word found for a given date or None if not found
input_date (int): date from user input in YYYYMMDD format
option (str): user's input choice for search type ('w' or 'd')
m (str): user-input month abbreviation
d (str): user-input day
y (str): user-input year
"""

# Lists to hold data from the file
data_lines = []        # Each line as [month, day, year, word]
dates = []             # Converted dates in YYYYMMDD format
answers = []           # Wordle answer words

# List of months used to convert text month to number
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Try to open the file and read the data
try:
    file = open("/workspaces/ICS3U_S2/Data/wordle.dat", "r")  # Open file in read mode
    line = file.readline().strip()                            # Read first line and strip whitespace
    while line != "":                                         # Loop until end of file
        data_lines.append(line.split())                      # Split line and add to data list
        line = file.readline().strip()                       # Read next line
    file.close()                                              # Close the file
except OSError as e:                                          # If file error happens
    print("File error:", e)                                   # Print error message
    exit()                                                    # Exit program

# Function to convert a month/day/year to a single number like YYYYMMDD
def to_number(mon, dy, yr):
    num = int(yr) * 10000                                     # Convert year to YYYY0000
    num += (months.index(mon) + 1) * 100                      # Convert month to MM00
    num += int(dy)                                            # Add day
    return num                                                # Return full date number

# Fill the dates and answers lists from the file data
for entry in data_lines:                                      # Loop through each entry in the file
    dates.append(to_number(entry[0], entry[1], entry[2]))     # Convert and store the date
    answers.append(entry[3])                                  # Store the word

# Search function to find the date a word was used
def search_word(word):
    word = word.upper()                                       # Make input uppercase
    if word in answers:                                       # If word exists in answer list
        index = answers.index(word)                           # Get its position
        return dates[index]                                   # Return date at that position
    return 0                                                  # Return 0 if not found

# Search function to find the word used on a given date
def search_date(mon, dy, yr):
    target = to_number(mon, dy, yr)                           # Convert input to date number
    if target in dates:                                       # If the date is in the list
        return answers[dates.index(target)]                   # Return corresponding word
    return None                                               # Return None if not found

# Start of program interaction
print("Welcome to the Wordle Finder!")                        # Greet the user

# Ask user to choose search type
option = input("Enter 'w' to search by word or 'd' to search by date: ").lower()  # Get and lowercase choice

# If searching by word
if option == "w":
    user_word = input("Enter a word to look up: ")            # Ask for the word
    found = search_word(user_word)                            # Search for its date
    if found > 0:                                             # If a match is found
        print("The word", user_word.upper(), "was used on", found)  # Show result
    else:
        print(user_word.upper(), "was not found.")            # Show not found message

# If searching by date
elif option == "d":
    y = input("Enter the year: ")                             # Ask for year
    m = input("Enter the month (e.g. Jan): ").capitalize()    # Ask for month and format it
    d = input("Enter the day: ")                              # Ask for day
    input_date = to_number(m, d, y)                           # Convert date to number

    if input_date < 20210619:                                 # Check if date is too early
        print(input_date, "is before the first Wordle. Try something later.")
    elif input_date > 20240421:                               # Check if date is too recent
        print(input_date, "is too recent. Our data only goes up to 20240421.")
    else:
        result = search_date(m, d, y)                         # Look up word for date
        if result != None:                                    # If word is found
            print("The word on", input_date, "was", result)   # Show result
        else:
            print("No word found for", input_date)            # Show not found message
