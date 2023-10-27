# Write a function to calculate the sum of digits of a number.
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

num = 12345
digit_sum = sum_of_digits(num)
print(digit_sum)
