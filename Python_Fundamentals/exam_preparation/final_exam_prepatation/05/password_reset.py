def take_odd(string):
    substr = ''
    for i in range(1, len(string), 2):
        substr += string[i]
    string = substr
    print(string)
    return string


def cut(index, length, string):
    string = string[:index] + string[index+length:]
    print(string)
    return string


def substitute_str(substring, substitute, string):
    if substring in string:
        string = string.replace(substring, substitute)
        print(string)
    else:
        print('Nothing to replace!')
    return string


string = input()

while True:
    commands = input().split()
    if commands[0] == 'Done':
        break
    elif commands[0] == 'TakeOdd':
        string = take_odd(string)
    elif commands[0] == 'Cut':
        index, length = int(commands[1]), int(commands[2])
        string = cut(index, length, string)
    elif commands[0] == 'Substitute':
        substring = commands[1]
        substitute = commands[2]
        string = substitute_str(substring, substitute, string)

print(f'Your password is: {string}')
