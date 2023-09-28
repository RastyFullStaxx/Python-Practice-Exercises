def str_str(haystack, needle):
    if not needle:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i

    return -1

# Example usage
haystack = "hello"
needle = "ll"
result = str_str(haystack, needle)
