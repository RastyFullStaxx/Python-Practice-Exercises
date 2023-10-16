# Write a Python program to read a text file and count the number of words.
with open("sample.txt", "r") as file:
    text = file.read()
    word_count = len(text.split())
    print(f"Word Count: {word_count}")
