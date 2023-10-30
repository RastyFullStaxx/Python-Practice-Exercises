# Write a list comprehension that extracts odd numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)
