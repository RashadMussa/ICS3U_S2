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

data_lines = []  # List to hold data lines from the file
dates = []       # List to store numeric dates
answers = []     # List to store corresponding Wordle words

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",  # Month abbreviations
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

file_loaded = True  # Flag to check if file loads successfully

try:
    file = open("/workspaces/ICS3U_S2/Data/wordle.dat", "r")  # Open the data file
    line = file.readline().strip()  # Read and strip first line
    while line != "":  # Loop until end of file
        data_lines.append(line.split())  # Add line as list of parts
        line = file.readline().strip()  # Read next line
    file.close()  # Close the file
except OSError as e:  # If file reading fails
    print("File error:", e)  # Show the error
    file_loaded = False  # Mark the file as not loaded

if file_loaded:  # Proceed only if file loaded correctly

    def to_number(mon, dy, yr):  # Convert month/day/year to numeric date
        num = int(yr) * 10000  # Start with year (YYYY0000)
        num += (months.index(mon) + 1) * 100  # Add month (MM00)
        num += int(dy)  # Add day
        return num  # Return full date

    for entry in data_lines:  # Loop through file entries
        dates.append(to_number(entry[0], entry[1], entry[2]))  # Convert and store date
        answers.append(entry[3])  # Store word

    def search_word(word):  # Look up date by word
        word = word.upper()  # Convert to uppercase
        if word in answers:  # If word exists in list
            index = answers.index(word)  # Get its index
            return dates[index]  # Return corresponding date
        return 0  # Return 0 if not found

    def search_date(mon, dy, yr):  # Look up word by date
        target = to_number(mon, dy, yr)  # Convert input to date number
        if target in dates:  # If date exists
            return answers[dates.index(target)]  # Return corresponding word
        return None  # Return None if date not found

    print("Welcome to the Wordle Finder!")  # Greeting

    option = input("Enter 'w' to search by word or 'd' to search by date: ").lower()  # Get search choice

    if option == "w":  # If user chose word search
        user_word = input("Enter a word to look up: ")  # Ask for the word
        found = search_word(user_word)  # Search for date
        if found > 0:  # If found
            print("The word", user_word.upper(), "was used on", found)  # Display result
        else:
            print(user_word.upper(), "was not found.")  # Word not found

    elif option == "d":  # If user chose date search
        y = input("Enter the year: ")  # Ask for year
        m = input("Enter the month (e.g. Jan): ").capitalize()  # Ask for month
        d = input("Enter the day: ")  # Ask for day
        input_date = to_number(m, d, y)  # Convert input to numeric date

        if input_date < 20210619:  # If too early
            print(input_date, "is before the first Wordle. Try something later.")
        elif input_date > 20240421:  # If too recent
            print(input_date, "is too recent. Our data only goes up to 20240421.")
        else:
            result = search_date(m, d, y)  # Search for word
            if result != None:  # If found
                print("The word on", input_date, "was", result)  # Show result
            else:
                print("No word found for", input_date)  # Date not found

else:
    print("Program ended because the Wordle data file could not be loaded.")  # File load failure message
