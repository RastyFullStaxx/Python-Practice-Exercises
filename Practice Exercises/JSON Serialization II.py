# Create a Python program that serializes and deserializes data using JSON.
import json

data = {"name": "Alice", "age": 30, "city": "Wonderland"}

# Serialize data to a JSON string
json_data = json.dumps(data)
print(json_data)

# Deserialize data from a JSON string
loaded_data = json.loads(json_data)
print(loaded_data)
