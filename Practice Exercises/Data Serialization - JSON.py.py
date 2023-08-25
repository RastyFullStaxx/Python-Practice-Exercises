import json

data = {
    "name": "Alice",
    "age": 30,
    "country": "USA"
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
