import csv

def parse_csv_to_list_of_dicts(filename):
    result = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            result.append(row)
    return result

# Test the function
filename = 'data.csv'  # Replace with the actual filename
data = parse_csv_to_list_of_dicts(filename)
print(data)
