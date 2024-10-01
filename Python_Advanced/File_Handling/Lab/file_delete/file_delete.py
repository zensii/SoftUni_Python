import os

to_delete = os.path.join("..", "file_writer", "my_first_file.txt")

try:
    os.remove(to_delete)
    print("File deleted!")
except FileNotFoundError:
    print("'File already deleted!'")