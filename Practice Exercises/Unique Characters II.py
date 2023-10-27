# Write a function that checks if a string has all unique characters.
def has_unique_characters(input_string):
    return len(set(input_string)) == len(input_string)

text = "abcdefg"
is_unique = has_unique_characters(text)
print(is_unique)
