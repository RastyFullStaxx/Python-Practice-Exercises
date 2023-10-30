# Create a function to check if a given year is a leap year.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

year = 2024
is_leap = is_leap_year(year)
print(is_leap)
