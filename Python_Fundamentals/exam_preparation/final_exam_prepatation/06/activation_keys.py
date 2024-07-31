def contains(substring, key):
    if substring in key:
        print(f"{key} contains {substring}")
    else:
        print(f"Substring not found!")


def flip(direction, start_index, end_index, key):

    sub = key[start_index:end_index]

    if direction == "Upper":
        sub = sub.upper()
    else:
        sub = sub.lower()

    key = key[:start_index] + sub + key[end_index:]
    print(key)
    return key


def slice(start_index, end_index, key):

    key = key[:start_index] + key[end_index:]
    print(key)
    return key


key = input()

while True:
    entry = input()
    if 'Generate'in entry:
        break
    command = entry.split('>>>')
    if command[0] == 'Contains':
        substring = command[1]
        contains(substring, key)
    elif command[0] == 'Flip':
        direction, start_index, end_index = command[1], int(command[2]), int(command[3])
        key = flip(direction, start_index, end_index, key)
    elif command[0] == 'Slice':
        start_index, end_index = int(command[1]), int(command[2])
        key = slice(start_index, end_index, key)

print(f"Your activation key is: {key}")