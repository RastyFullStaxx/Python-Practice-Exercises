# Create a function that finds all occurrences of a substring in a given string.
def find_substring_occurrences(text, substring):
    occurrences = [i for i in range(len(text)) if text.startswith(substring, i)]
    return occurrences

input_text = "ababababab"
sub = "ab"
substring_occurrences = find_substring_occurrences(input_text, sub)
print(substring_occurrences)
