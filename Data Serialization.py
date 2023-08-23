import json

data = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}

# Serialization
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)

# Deserialization
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)

print(loaded_data)
