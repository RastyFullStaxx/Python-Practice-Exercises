def reverse_words_in_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

input_sentence = "Hello world, this is Python."
reversed_sentence = reverse_words_in_sentence(input_sentence)
print(reversed_sentence)
