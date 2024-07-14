def decode(strings, key):

    decoded_message = []

    for string in strings:
        decoded_string = ''
        for index in range(len(string)):
            decoded_string += chr(ord(string[index]) - int(key[index % len(key)]))
        decoded_message.append(decoded_string)

    return decoded_message


def read_message(decoded_message):

    for treasure in decoded_message:
        type_start_index = None
        type_end_index = None
        for index, char in enumerate(treasure):
            if char == '&':
                if type_start_index is None:
                    type_start_index = index+1
                elif type_end_index is None:
                    type_end_index = index
                    break
        treasure_type = treasure[type_start_index:type_end_index]

        coord_start_index = treasure.index('<')
        coord_end_index = treasure.index('>')
        coordinates = treasure[coord_start_index+1:coord_end_index]

        print(f'Found {treasure_type} at {coordinates}')


key = input().split()
strings = []
string_input = input()

while string_input != 'find':
    strings.append(string_input)
    string_input = input()

decoded_message = decode(strings, key)
read_message(decoded_message)
