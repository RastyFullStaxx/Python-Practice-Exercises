def pig_latin_translator(text):
    words = text.split()
    pig_latin_words = []
    vowels = "aeiouAEIOU"
    for word in words:
        if word[0] in vowels:
            pig_latin_word = word + "way"
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                i += 1
            pig_latin_word = word[i:] + word[:i] + "ay"
        pig_latin_words.append(pig_latin_word)
    return ' '.join(pig_latin_words)

sentence = "Hello World"
pig_latin_sentence = pig_latin_translator(sentence)
print(pig_latin_sentence)
