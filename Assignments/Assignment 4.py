"""
Author : Rashad Mussa
Course code: ICS3U
Revision date : May 19, 2025
Program : Wordle Database Search
Description : A program that reads from a Wordle solution file and allows the user to 
    search for a Wordle solution by date or find the date on which a specific word appeared.

VARIABLE DICTIONARY:
  file_path (str) = absolute path to the wordle.dat file containing the Wordle solutions
  arr (list) = stores each line from the file as a list: [Month, Day, Year, Word]
  date_arr (list) = stores converted dates in integer YYYYMMDD format for each word
  word_arr (list) = stores all Wordle solution words from the file
  months (list) = 3-letter month abbreviations used to convert month names into numeric values
  fh (file object) = file handle used to open and read the wordle.dat file
  line (str) = temporarily holds each line read from the file
  parts (list) = list of elements split from each line in the format [month, day, year, word]
  entry (list) = each individual line from arr used to extract and process date and word
  month (str) = 3-letter abbreviation of a month from file or user input
  day (str) = day component of a date from file or user input
  year (str) = year component of a date from file or user input
  word (str) = Wordle solution associated with a specific date, from file or function result
  user_word (str) = word entered by the user during a word search
  index (int) = index of a found word or date in the respective array
  date (int) = combined integer date in YYYYMMDD format, either from file or user input
  choice (str) = user's choice between searching by word ('w') or date ('d')
  w (str) = word input by the user if they choose to search by word

"""


# File path to the uploaded wordle.dat
file_path = "/workspaces/ICS3U_S2/Data/wordle.dat"

# Arrays for data
arr = []
date_arr = []
word_arr = []

# Month conversion helper
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Reads and parses the wordle.dat file
try:
    with open(file_path, "r") as fh:
        for line in fh:
            parts = line.strip().split()
            if len(parts) == 4:
                arr.append(parts)
except OSError as err:
    print("OSError:", err)
    exit()

# Function to convert month, day, year -> YYYYMMDD
def merge(month, day, year):
    month_num = (months.index(month) + 1) * 100
    year_num = int(year) * 10000
    day_num = int(day)
    return year_num + month_num + day_num

# Fill date_arr and word_arr
for entry in arr:
    month, day, year, word = entry
    date_arr.append(merge(month, day, year))
    word_arr.append(word)

# Search by word
def isWordMatch(user_word):
    user_word = user_word.upper()
    if user_word in word_arr:
        index = word_arr.index(user_word)
        return date_arr[index]
    return 0

# Search by date
def isDateMatch(month, day, year):
    date = merge(month, day, year)
    if date in date_arr:
        index = date_arr.index(date)
        return word_arr[index]
    return None

# Main interface
print("Welcome to the Wordle Database!")
choice = input("Enter w if you are looking for a word, or d for a word on a certain date: ").lower()

if choice == 'w':
    w = input("What word are you looking for? ")
    date = isWordMatch(w)
    if date:
        print("The word {} was the solution to the puzzle on {}.".format(w.upper(), date))
    else:
        print("{} was not found in the database.".format(w.upper()))

elif choice == 'd':
    year = input("Enter the year: ")
    month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ").capitalize()
    day = input("Enter the day: ")
    date = merge(month, day, year)

    if date < 20210619:
        print("{} is too early. No wordles occurred before 20210619. Enter a later date.".format(date))
    elif date > 20240421:
        print("{} is too recent. Our records only go as late as 20240421. Please enter an earlier date.".format(date))
    else:
        word = isDateMatch(month, day, year)
        if word:
            print("The word entered on {} was {}.".format(date, word))
        else:
            print("No word found for date {}.".format(date))
