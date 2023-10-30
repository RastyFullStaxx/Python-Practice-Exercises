# Create a function to determine if a number is a power of two.
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

number = 16
is_power_of_2 = is_power_of_two(number)
print(is_power_of_2)
