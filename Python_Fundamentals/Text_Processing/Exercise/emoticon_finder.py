message = input()

for index in range(len(message)):
    if message[index] == ':':
        print(message[index:index+2])
