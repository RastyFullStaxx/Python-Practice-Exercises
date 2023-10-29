# Create a function that counts the occurrences of words in a string.
def word_count(text):
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

text = "This is a sample sentence. This sentence is a sample."
counts = word_count(text)
print(counts)
