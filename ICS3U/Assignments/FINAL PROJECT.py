"""
Author : Rashad
Student number: 762918
Course code: ICS3U
Revision date : June 12, 2025
Program : Expired Credit Cards Report
Description : Reads credit card data from a file, checks card validity with Luhn algorithm,
              identifies expired or soon-to-expire cards, sorts them by expiry date,
              and outputs a detailed report with color-coded console messages.

VARIABLE DICTIONARY:
cc_number (str) = credit card number string passed into luhn_check()
total (int) = sum of digits used in Luhn checksum calculation
reverse_digits (str) = reversed string of cc_number for Luhn processing
i (int) = loop index for iterating over digits in reversed credit card number
n (int) = integer digit currently processed in Luhn algorithm
records (list) = list of card records being sorted in merge_sort()
mid (int) = midpoint index to split records into left and right halves
left (list) = left half of records list in merge_sort()
right (list) = right half of records list in merge_sort()
i, j, k (int) = indices for iterating left, right, and main records lists in merge_sort()
input_file (str) = file path for input data of credit cards
output_file (str) = file name to write expired cards report
threshold (int) = integer YYYYMM format representing the cutoff date for expiry checking
expired (list) = list of records containing expired or soon-to-expire cards
RED, YELLOW, RESET (str) = ANSI color escape codes for console output
file (file object) = input file handle for reading card data
lines (list) = list of all lines read from the input file
line (str) = current line read from file during processing
parts (list) = list of fields parsed from a line by splitting on commas
fname (str) = first name extracted from line data
lname (str) = last name extracted from line data
cctype (str) = credit card type extracted from line data
ccnum (str) = credit card number extracted from line data
month (int) = expiry month extracted and converted to integer
year (int) = expiry year extracted and converted to integer
dateval (int) = combined integer YYYYMM format of expiry date used for comparison and sorting
status (str) = "EXPIRED" or "RENEW IMMEDIATELY" depending on expiry date
name (str) = formatted full name padded for alignment
expiry (str) = formatted expiry date string in YYYYMM format
item (list) = single record from expired list used during output
color (str) = chosen ANSI color code string depending on status
"""

# ANSI color codes as constants at top for clarity
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def luhn_check(cc_number):
    """
    Validates a credit card number string using the Luhn algorithm.
    Returns True if valid, False otherwise.
    """
    total = 0  # Initialize sum for checksum
    reverse_digits = cc_number[::-1]  # Reverse number for processing from right to left

    for i in range(len(reverse_digits)):  # Loop through each digit by index
        n = int(reverse_digits[i])  # Convert character to integer
        if i % 2 == 1:  # Every second digit (odd index in reversed)
            n *= 2  # Double it
            if n > 9:  # If result is two digits, subtract 9 (sum of digits)
                n -= 9
        total += n  # Add to total sum

    return total % 10 == 0  # Valid if total modulo 10 is zero


def merge_sort(records):
    """
    Sorts the list of card records in place by expiry date (YYYYMM format) using merge sort.
    Each record is a list with the expiry date as the last element.
    """
    if len(records) > 1:  # Only sort if more than one element
        mid = len(records) // 2  # Find middle
        left = records[:mid]  # Split left half
        right = records[mid:]  # Split right half

        merge_sort(left)  # Recursively sort left half
        merge_sort(right)  # Recursively sort right half

        i = j = k = 0  # Initialize indices for left, right, and merged list

        # Merge left and right halves back into records
        while i < len(left) and j < len(right):
            if left[i][-1] < right[j][-1]:  # Compare expiry dates
                records[k] = left[i]
                i += 1
            else:
                records[k] = right[j]
                j += 1
            k += 1

        # Append any remaining elements from left half
        while i < len(left):
            records[k] = left[i]
            i += 1
            k += 1

        # Append any remaining elements from right half
        while j < len(right):
            records[k] = right[j]
            j += 1
            k += 1


def parse_line(line):
    """
    Parses a single line of input data into its components,
    validates, and returns a record if valid.
    Returns None if line is invalid or improperly formatted.
    """
    parts = line.strip().split(",")  # Split CSV fields

    if len(parts) != 6:
        return None  # Invalid number of fields

    fname, lname, cctype, ccnum_str, month_str, year_str = parts

    # Validate credit card number digits only
    if not ccnum_str.isdigit():
        return None

    try:
        month = int(month_str)
        year = int(year_str)
    except ValueError:
        return None  # Month/year not integers

    # Validate month is in valid range
    if not (1 <= month <= 12):
        return None

    dateval = year * 100 + month  # Combine year and month for easy comparison

    return [fname, lname, cctype, ccnum_str, month, year, dateval]


def output_report(expired_cards, output_file):
    """
    Prints the expired cards report to the console with colors and writes to a file.
    Includes header and summary lines.
    """
    if not expired_cards:  # No expired cards found
        print(RED + "No expired or soon-to-expire credit cards found." + RESET)
        with open(output_file, "w") as out:
            out.write("No expired or soon-to-expire credit cards found.\n")
        return

    header = "{:<20} {:<12} {:<20} {:<6} {}".format("Name", "Card Type", "Number", "Expiry", "Status")
    separator = "-" * 70

    print(header)
    print(separator)

    with open(output_file, "w") as out:
        out.write(header + "\n")
        out.write(separator + "\n")

        for item in expired_cards:
            color = RED if item[4] == "EXPIRED" else YELLOW  # Color based on status
            line = "{:<20} {:<12} {:<20} {:<6} {}".format(item[0], item[1], item[2], item[3], item[4])
            print(color + line + RESET)  # Print colored line to console
            out.write(line + "\n")  # Write line to output file

        summary = "\nTotal expired/renew immediately cards: {}".format(len(expired_cards))
        print(summary)
        out.write(summary + "\n")


def main():
    input_file = "/workspaces/ICS3U_S2/ICS3U/Data/CARDNUMBERS.dat"  # Input file path
    output_file = "expired_cards_report.txt"  # Output file name
    threshold = 202506  # Threshold date in YYYYMM (June 2025)

    expired = []  # List to hold expired or soon-to-expire cards

    try:
        with open(input_file, "r") as file:  # Open input file safely
            lines = file.readlines()  # Read all lines

        for line in lines[1:]:  # Skip header line and process remaining lines
            record = parse_line(line)  # Parse and validate line

            if record is None:  # Skip invalid lines
                continue

            fname, lname, cctype, ccnum, month, year, dateval = record

            # Only consider cards expired or expiring at or before threshold AND that pass Luhn check
            if dateval <= threshold and luhn_check(ccnum):
                # Determine status string
                status = "EXPIRED" if dateval < threshold else "RENEW IMMEDIATELY"

                name = (fname + " " + lname + ":").ljust(20)  # Format name for alignment
                cctype = cctype.ljust(12)  # Format card type
                ccnum = "#" + ccnum  # Prefix card number for output
                expiry = str(year) + str(month).zfill(2)  # Format expiry as YYYYMM string

                # Append all necessary fields plus dateval for sorting
                expired.append([name, cctype, ccnum, expiry, status, dateval])

        merge_sort(expired)  # Sort expired cards by expiry date ascending

        output_report(expired, output_file)  # Output the results

    except FileNotFoundError:  # Handle missing input file
        print(RED + "Error: CARDNUMBERS.dat not found at the given path." + RESET)

    except Exception as e:  # Catch any other unexpected errors gracefully
        print(RED + "An unexpected error occurred: " + str(e) + RESET)


if __name__ == "__main__":
    main()
