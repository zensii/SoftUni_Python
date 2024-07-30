def insert_space(pos_index, coded_message):

    coded_message = coded_message[:pos_index] + ' ' + coded_message[pos_index:]
    print(coded_message)
    return coded_message


def reverse(substring, coded_message):

    if substring in coded_message:
        coded_message = coded_message.replace(substring, '', 1)
        coded_message = coded_message + substring[::-1]
        print(coded_message)
    else:
        print('error')

    return coded_message


def change_all(substring, replacement, coded_message):

    coded_message = coded_message.replace(substring, replacement)
    print(coded_message)

    return coded_message


def process_cmd(all_commands: list, coded_message):
    for entry in all_commands:
        action, *parameter = entry.split(':|:')
        if action == 'InsertSpace':
            index = int(parameter[0])
            coded_message = insert_space(index, coded_message)
        elif action == 'Reverse':
            substring = parameter[0]
            coded_message = reverse(substring, coded_message)
        elif action == 'ChangeAll':
            substring = parameter[0]
            replacement = parameter[1]
            coded_message = change_all(substring, replacement, coded_message)

    return coded_message


coded_msg = input()
commands = []

while True:
    command = input()
    if command == 'Reveal':
        break
    else:
        commands.append(command)

decoded_msg = process_cmd(commands, coded_msg)

print(f'You have a new text message: {decoded_msg}')
