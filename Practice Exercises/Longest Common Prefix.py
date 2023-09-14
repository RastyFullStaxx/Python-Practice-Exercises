def longest_common_prefix(strings):
    if not strings:
        return ""

    min_len = min(len(s) for s in strings)
    prefix = ""

    for i in range(min_len):
        char = strings[0][i]
        if all(s[i] == char for s in strings):
            prefix += char
        else:
            break

    return prefix

words = ["flower", "flow", "flight"]
result = longest_common_prefix(words)
print(result)
