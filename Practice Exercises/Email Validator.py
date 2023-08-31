import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

email1 = "user@example.com"
email2 = "invalid.email"
email3 = "name@domain"
print(f"{email1}: {validate_email(email1)}")
print(f"{email2}: {validate_email(email2)}")
print(f"{email3}: {validate_email(email3)}")
