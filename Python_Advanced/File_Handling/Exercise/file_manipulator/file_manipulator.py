def create_file(file_name):
    with open(file_name, "w") as file:
        pass


def add_content(file_name, content):
     try:
         with open(file_name, 'a') as file:
             file.write(content + '\n')
     except FileNotFoundError:
         create_file(file_name)
         add_content(file_name, content)


def replace_string(file_name, old, new ):
    try:
        with open(file_name, "r") as file:
            contents = file.read()
            contents = contents.replace(old, new)
        with open(file_name, 'w') as file:
            file.write(contents)

    except FileNotFoundError:
        print("An error occurred")


def delete(file_name):
    import os

    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


commander = {
    'Create': create_file,
    'Add': add_content,
    'Replace': replace_string,
    'Delete': delete
}

while True:
    command = input()
    if command == 'End':
        break

    command, *params = command.split('-')
    commander[command](*params)
