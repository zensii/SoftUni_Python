try:
    file_obj = open("text.txt")
    print("File is found")
except FileNotFoundError:
    print("File not found")
