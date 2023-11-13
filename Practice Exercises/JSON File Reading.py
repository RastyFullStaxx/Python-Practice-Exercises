# Read data from a JSON file and extract information.
import json

with open("data.json", "r") as file:
    data = json.load(file)

# Access specific information from the loaded JSON data
print(data["name"])
