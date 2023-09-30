import pickle

data = {"name": "Alice", "age": 30, "city": "Wonderland"}

# Serialize data to a file
with open("data.pickle", "wb") as file:
    pickle.dump(data, file)

# Deserialize data from the file
with open("data.pickle", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)
