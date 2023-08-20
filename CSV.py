import csv

data = [
    ["Name", "Age", "Country"],
    ["Alice", 25, "USA"],
    ["Bob", 30, "Canada"]
]

with open("data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
