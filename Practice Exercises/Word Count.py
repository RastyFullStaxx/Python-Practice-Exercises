def word_count(sentence):
    words = sentence.split()
    word_freq = {}
    for word in words:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

sentence = "This is a test sentence. This sentence is a test."
word_frequency = word_count(sentence)
print(word_frequency)
