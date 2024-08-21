def exchange(index, array):
    if 0 <= index < len(array):
        sub1 = array[:index+1]
        sub2 = array[index+1:]
        array = sub2 + sub1
    else:
        print('Invalid index')
    return array


def max_even(array):
    cur_max_even = None
    max_index = None
    for index, value in enumerate(array):
        if value % 2 == 0:
            if cur_max_even is None:
                cur_max_even = value
                max_index = index
            else:
                if value >= cur_max_even:
                    cur_max_even = value
                    max_index = index
    if max_index is not None:
        return max_index
    else:
        return 'No matches'

    # maxx = max((pair for pair in enumerate(array) if pair[1] % 2 == 0), key=lambda x: (x[1], x[0]), default=(-1, None))[0]
    #
    # if maxx != -1:
    #     return maxx
    # else:
    #     return 'No matches'


def max_odd(array):

    maxx = max((pair for pair in enumerate(array) if pair[1] % 2 != 0), key=lambda x: (x[1], x[0]), default=(-1, None))[0]

    if maxx != -1:
        return maxx
    else:
        return 'No matches'


def min_even(array):

    minn = sorted(list(filter(lambda x: x[1] % 2 == 0, enumerate(array))), key=lambda x: (x[1], -x[0]))

    if minn:
        return minn[0][0]
    else:
        return 'No matches'


def min_odd(array):

    minn = sorted(list(filter(lambda x: x[1] % 2 != 0, enumerate(array))), key=lambda x: (x[1], -x[0]))

    if minn:
        return minn[0][0]
    else:
        return 'No matches'


def first_count_even(count, array):

    if count > len(array):
        return 'Invalid count'
    else:
        return list(filter(lambda x: x % 2 == 0, array))[:count]


def first_count_odd(count, array):

    if count > len(array):
        return 'Invalid count'
    else:
        return list(filter(lambda x: x % 2 != 0, array))[:count]


def last_count_even(count, array):

    if count > len(array):
        return 'Invalid count'
    else:
        return list(filter(lambda x: x % 2 == 0, array))[-1:-count-1:-1][::-1]


def last_count_odd(count, array):

    if count > len(array):
        return 'Invalid count'
    else:
        return list(filter(lambda x: x % 2 != 0, array))[-1:-count-1:-1][::-1]


array = [int(digit) for digit in input().split()]

while True:
    usr_input = input()
    command = usr_input.split()

    if command[0] == 'exchange':

            index = int(command[1])
            array = exchange(index, array)

    elif command[0] == 'max':
            if command[1] == 'even':
                print(max_even(array))
            else:
                print(max_odd(array))

    elif command[0] == 'min':
            if command[1] == 'even':
                print(min_even(array))
            else:
                print(min_odd(array))

    elif command[0] == 'first':
            count = int(command[1])
            if command[-1] == 'even':

                print(first_count_even(count, array))
            else:
                print(first_count_odd(count, array))

    elif command[0] == 'last':
            count = int(command[1])
            if command[-1] == 'even':

                print(last_count_even(count, array))
            else:
                print(last_count_odd(count, array))

    elif command[0] == 'end':
            break

print(array)
