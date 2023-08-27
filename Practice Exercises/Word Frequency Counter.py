import re
from collections import Counter

def word_frequency(text):
    words = re.findall(r'\w+', text.lower())
    word_count = Counter(words)
    return word_count

text = "This is a sample text. It is just a sample."
frequency = word_frequency(text)
print(frequency)
