def shoot(targets, index, power):

    if 0 <= index < len(targets):

        targets[index] -= power

        if targets[index] <= 0:
            targets.pop(index)

    return targets


def add(targets, index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print('Invalid placement!')
    return targets


def strike(targets, index, radius):
    if 0 <= index-radius <= index <= index+radius < len(targets):
        targets[index-radius:index+radius+1] = []
    else:
        print('Strike missed!')
    return targets


def main():
    targets_state = [num for num in map(int, input().split())]
    command = input()
    while True:

        command = command.split()

        if command[0] == 'End':
            print('|'.join(target for target in map(str, targets_state)))
            break
        elif command[0] == 'Shoot':
            shoot(targets_state, int(command[1]), int(command[2]))

        elif command[0] == 'Add':
            add(targets_state, int(command[1]), int(command[2]))

        elif command[0] == 'Strike':
            strike(targets_state, int(command[1]), int(command[2]))

        command = input()


if __name__ == '__main__':
    main()