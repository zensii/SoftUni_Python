import re


def upper(index, password):

    modified_char = password[index].upper()
    password = password[:index] + modified_char + password[index+1:]
    print(password)
    return password


def lower(index, password):

    modified_char = password[index].lower()
    password = password[:index] + modified_char + password[index+1:]
    print(password)
    return password


def insert(index, char, password):

    if 0 <= index < len(password):
        password = password[:index] + char + password[index:]
        print(password)
    return password


def replace(char, value, password):
    replacement_char = chr(ord(char) + value)
    if char in password:
        password = password.replace(char, replacement_char)
        print(password)
    return password


def validation(password):
    if len(password) < 8:
        print(f"Password must be at least 8 characters long!")
    if password not in re.findall(r'\w+', password):
        print(f"Password must consist only of letters, digits and _!")
    if re.search(r'[A-Z]', password) is None:
        print(f"Password must consist at least one uppercase letter!")
    if re.search(r'[a-z]', password) is None:
        print(f"Password must consist at least one lowercase letter!")
    if re.search(r'[0-9]', password) is None:
        print(f"Password must consist at least one digit!")


string = input()
commands = []

while True:
    command = input()
    if command == 'Complete':
        break
    commands.append(command)

for command in commands:
    operation = command.split()

    if operation[0] == 'Validation':
        validation(string)
    elif operation[1] == 'Upper':
        string = upper(int(operation[2]), string)
    elif operation[1] == 'Lower':
        string = lower(int(operation[2]), string)
    elif operation[0] == 'Insert':
        string = insert(int(operation[1]), operation[2], string)
    elif operation[0] == 'Replace':
        string = replace(operation[1], int(operation[2]), string)