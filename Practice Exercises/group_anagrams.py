def group_anagrams(words):
    anagram_groups = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    return list(anagram_groups.values())

word_list = ["listen", "silent", "hello", "world", "act", "cat"]
anagram_lists = group_anagrams(word_list)
print(anagram_lists)
