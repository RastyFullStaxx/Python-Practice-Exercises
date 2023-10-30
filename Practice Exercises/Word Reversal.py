# Implement a function to reverse the order of words in a sentence.
def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence

input_sentence = "This is a sample sentence."
reversed_sentence = reverse_words(input_sentence)
print(reversed_sentence)
