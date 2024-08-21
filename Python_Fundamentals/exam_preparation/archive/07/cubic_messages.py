import re


def check_validity(n, coded):
    regex = rf'^\d+([a-zA-Z]{{{n}}})[^a-zA-Z]*$'
    valid = re.findall(regex, coded)
    if valid:
        return valid


def get_indices(usr_input):
    regex = r'\d'
    indices = re.findall(regex, usr_input)
    return indices


def get_verification(indices, message):
    ver_code = ''

    for index_num in indices:
        if 0 <= index_num < len(message):
            ver_code += message[index_num]
        else:
            ver_code += ' '
    return ver_code


messages = []

while True:

    usr_input = input()

    if usr_input == 'Over!':
        break

    n = int(input())

    message = check_validity(n, usr_input)
    if message:
        indices = [int(indx) for indx in get_indices(usr_input)]
        ver_code = get_verification(indices, message[0])
        print(f"{message[0]} == {ver_code}")
