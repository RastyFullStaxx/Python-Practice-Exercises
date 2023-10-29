# Create a function to check if a number is a perfect number.
def is_perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

number = 28
is_perfect = is_perfect_number(number)
print(is_perfect)
