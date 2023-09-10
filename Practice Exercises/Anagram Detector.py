def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

word1 = "listen"
word2 = "silent"
word3 = "hello"
print(are_anagrams(word1, word2))
print(are_anagrams(word1, word3))
