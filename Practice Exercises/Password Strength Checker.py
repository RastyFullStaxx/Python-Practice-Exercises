import re

def is_strong_password(password):
    return (
        len(password) >= 8 and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password)
    )

password1 = "StrongP@ssw0rd"
password2 = "weak"
print(f"{password1}: {is_strong_password(password1)}")
print(f"{password2}: {is_strong_password(password2)}")
