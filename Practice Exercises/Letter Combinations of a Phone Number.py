def letter_combinations(digits):
    if not digits:
        return []

    phone_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }

    result = ['']
    for digit in digits:
        result = [prefix + letter for prefix in result for letter in phone_letters[digit]]

    return result

phone_number = "23"
result = letter_combinations(phone_number)
