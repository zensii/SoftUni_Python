message = input()
unique_chars = set()
rage_message_strings = []
rage_message_repeats = []
current_char_set = ''
index = 0
current_num = ''
while index < len(message):
    if message[index].isdigit():
        while index < len(message) and message[index].isdigit():
            current_num += message[index]
            index += 1
        rage_message_repeats.append(int(current_num))
        rage_message_strings.append(current_char_set)
        current_char_set = ''
        current_num = ''
    else:
        unique_chars.add(message[index].upper())
        current_char_set += message[index].upper()
        index += 1

print(f'Unique symbols used: {len(unique_chars)}')
print(''.join([a * b for a, b in zip(rage_message_strings, rage_message_repeats)]))

