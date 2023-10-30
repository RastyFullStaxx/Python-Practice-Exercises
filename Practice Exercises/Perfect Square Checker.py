# Write a function to check if a given number is a perfect square.
def is_perfect_square(n):
    return n >= 0 and int(n**0.5) ** 2 == n

number = 25
is_perfect = is_perfect_square(number)
print(is_perfect)
