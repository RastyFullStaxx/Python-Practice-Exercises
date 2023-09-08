def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

word1 = "racecar"
word2 = "hello"
print(f"{word1}: {is_palindrome(word1)}")
print(f"{word2}: {is_palindrome(word2)}")
