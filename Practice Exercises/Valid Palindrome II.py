def valid_palindrome(s):
    def is_palindrome(s):
        return s == s[::-1]

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome(s[left:right]) or is_palindrome(s[left + 1:right + 1])
        left += 1
        right -= 1
    return True

text1 = "aba"
text2 = "abca"
print(valid_palindrome(text1))
print(valid_palindrome(text2))
