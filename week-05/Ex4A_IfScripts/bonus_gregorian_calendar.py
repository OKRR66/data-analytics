#bonus_gregorian_calendar

# In a file named bonus_gregorian_calendar.py, create a script to determine whether a given year is a leap year in the Gregorian calendar. 
# You will need to do a little research to determine exactly what makes a year a leap year.
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
# Run it several times with different values for the year. Make sure to test the years 1900, 1950, 1999, 2000, 2001, and 20212.

