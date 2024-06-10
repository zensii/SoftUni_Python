def swap(array):
    index_1 = int(command[1])
    index_2 = int(command[2])
    array[index_1], array[index_2] = array[index_2], array[index_1]
    return array


def multipy(array):
    index_1 = int(command[1])
    index_2 = int(command[2])
    array[index_1] = array[index_1] * array[index_2]
    return array


def decrease(array):
    for i in range(len(array)):
        array[i] -= 1
    return array


array = [digit for digit in map(int, (input().split(' ')))]
command = input()

while command != 'end':
    command = command.split(' ')
    if command[0] == 'swap':
        swap(array)
    elif command[0] == 'decrease':
        decrease(array)
    elif command[0] == 'multiply':
        multipy(array)

    command = input()

string = map(str, array)
print(', '.join(string))
