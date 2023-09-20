def group_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    return list(anagrams.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
