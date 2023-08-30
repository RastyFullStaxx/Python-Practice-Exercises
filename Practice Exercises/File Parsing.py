import csv

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

csv_filename = 'data.csv'
read_csv_file(csv_filename)
