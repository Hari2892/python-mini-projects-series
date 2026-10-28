
import calendar

try:
    year = int(input("ENTER YEAR: "))
    month = int(input("ENTER MONTH: "))

    if year < 1:
        print("ERROR: Year must be a positive integer.")

    elif month < 1 or month > 12:
        print("ERROR: Month must be between 1 and 12.")

    else:
        print("\n", calendar.month(year, month))

except ValueError:
    print("ERROR: Please enter integers only.")
