# Implement a simple file encryption and decryption using a key.
def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted_data = bytes(x ^ key for x in data)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    encrypt_file(input_file, output_file, key)  # Decryption is the same as encryption

# Example usage
encrypt_file("secret.txt", "encrypted_secret.txt", 42)
decrypt_file("encrypted_secret.txt", "decrypted_secret.txt", 42)
