def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year1 = 2024
year2 = 2100
print(f"{year1}: {is_leap_year(year1)}")
print(f"{year2}: {is_leap_year(year2)}")
