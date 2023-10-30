# Implement a function to determine if a number is odd or even.
def is_odd_or_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = 7
odd_or_even = is_odd_or_even(number)
print(odd_or_even)
