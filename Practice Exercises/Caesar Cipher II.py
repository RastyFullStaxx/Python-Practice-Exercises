# Implement a Caesar cipher encryption and decryption function.
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            else:
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

message = "Hello, World!"
shift_value = 3
encrypted_message = caesar_cipher(message, shift_value)
print(encrypted_message)
