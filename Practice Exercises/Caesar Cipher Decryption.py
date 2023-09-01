def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            shift_amount = (ord(char) - ord('a') - shift) % 26
            decrypted_char = chr(ord('a') + shift_amount)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

encrypted_text = "khoor zruog"
shift = 3
decrypted_text = caesar_decrypt(encrypted_text, shift)
print(decrypted_text)
