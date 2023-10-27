# Write a function that finds the longest substring of consecutive characters in a string.
def find_longest_consecutive_chars(input_string):
    max_length = 0
    current_length = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    return max(max_length, current_length)

input_string = "aaabbbbcc"
max_consecutive_chars = find_longest_consecutive_chars(input_string)
print(max_consecutive_chars)
