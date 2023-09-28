def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

# Example usage
string = "A man, a plan, a canal: Panama"
result = is_palindrome(string)
print(result)  # Output: True
