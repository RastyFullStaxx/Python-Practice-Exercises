# Create a function to list all files in a directory with a specific file extension.
import os

def list_files_with_extension(directory, extension):
    files = [file for file in os.listdir(directory) if file.endswith(extension)]
    return files

directory_path = "/path/to/directory"
file_extension = ".txt"
files_with_extension = list_files_with_extension(directory_path, file_extension)
print(files_with_extension)
