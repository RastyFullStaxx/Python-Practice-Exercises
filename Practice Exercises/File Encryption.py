def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = (ord(char) - ord('a') + shift) % 26
            encrypted_char = chr(ord('a') + shift_amount)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

input_filename = 'input.txt'
output_filename = 'output.txt'
shift = 3
with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    content = input_file.read()
    encrypted_content = caesar_cipher(content, shift)
    output_file.write(encrypted_content)
