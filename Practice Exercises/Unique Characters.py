def has_unique_characters(s):
    return len(set(s)) == len(s)

text1 = "python"
text2 = "hello"
print(f"{text1}: {has_unique_characters(text1)}")
print(f"{text2}: {has_unique_characters(text2)}")
