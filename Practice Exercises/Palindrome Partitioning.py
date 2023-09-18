def partition_palindromes(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path)
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                backtrack(end, path + [s[start:end]])

    result = []
    backtrack(0, [])
    return result

string = "aab"
result = partition_palindromes(string)
print(result)
