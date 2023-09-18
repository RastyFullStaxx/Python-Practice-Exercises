def is_anagram(s, t):
    return sorted(s) == sorted(t)

string1 = "anagram"
string2 = "nagaram"
result = is_anagram(string1, string2)
print(result)
