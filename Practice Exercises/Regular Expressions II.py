import re

text = "Contact us at info@example.com or support@website.org for assistance."

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
matches = re.findall(pattern, text)

for match in matches:
    print(match)
