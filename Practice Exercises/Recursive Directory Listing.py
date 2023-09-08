import os

def list_files_in_directory(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

directory_path = "/path/to/your/directory"
files = list_files_in_directory(directory_path)
for file in files:
    print(file)
