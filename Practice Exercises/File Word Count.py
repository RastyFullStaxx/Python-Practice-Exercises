def count_words_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

file_name = 'sample.txt'
word_count = count_words_in_file(file_name)
print(f"Word count in {file_name}: {word_count}")
