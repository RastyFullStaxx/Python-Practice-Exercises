# Implement a function that generates a random password with a specified length.
import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

random_password = generate_random_password(12)
print(random_password)
