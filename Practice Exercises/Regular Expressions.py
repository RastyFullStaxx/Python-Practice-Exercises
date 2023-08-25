import re

pattern = r"\b\w{4}\b"
text = "This is a test sentence with some words of different lengths."

matches = re.findall(pattern, text)
print(matches)
