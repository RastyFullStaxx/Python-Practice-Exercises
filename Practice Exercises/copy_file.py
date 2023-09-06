def copy_file(source_filename, destination_filename):
    with open(source_filename, 'r') as source_file:
        data = source_file.read()
        with open(destination_filename, 'w') as destination_file:
            destination_file.write(data)

source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)
