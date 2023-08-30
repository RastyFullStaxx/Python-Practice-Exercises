def caesar_cipher(text, shift):
    encrypted = ''
    for char in text:
        if char.isalpha():
            shift_amount = (ord(char) - ord('a') + shift) % 26
            encrypted_char = chr(ord('a') + shift_amount)
            encrypted += encrypted_char
        else:
            encrypted += char
    return encrypted

text = "hello world"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print(encrypted_text)
