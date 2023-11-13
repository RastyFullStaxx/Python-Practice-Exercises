# Write a function to check if a number is an Armstrong number.
def is_armstrong_number(n):
    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
    return armstrong_sum == n

number = 1634
is_armstrong = is_armstrong_number(number)
print(is_armstrong)
