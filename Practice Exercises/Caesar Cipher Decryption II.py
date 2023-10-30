# Write a function to decrypt a Caesar cipher given the encrypted text and shift value.
def caesar_decryption(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
            else:
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

cipher_text = "Khoor, Zruog!"
shift_value = 3
decrypted_text = caesar_decryption(cipher_text, shift_value)
print(decrypted_text)
