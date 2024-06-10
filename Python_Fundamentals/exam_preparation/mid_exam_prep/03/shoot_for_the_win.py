def hit(targets, index):

    current_target_value = targets.pop(index)

    for i in range(len(targets)):
        if targets[i] > current_target_value:
            targets[i] -= current_target_value
        elif targets[i] != -1 and targets[i] <= current_target_value:
            targets[i] += current_target_value

    targets.insert(index, -1)

    return targets


def check_hit(targets, target_index):

    if 0 <= target_index < len(targets):

        hit(targets, target_index)
        return targets, 1
    else:
        return targets, 0


def main():

    target_points = [value for value in map(int, input().split(' '))]
    command = input()
    hits = 0
    while command != 'End':

        index = int(command)

        hits += check_hit(target_points, index)[1]

        command = input()
    final_state = (target for target in map(str, target_points))
    print(f'Shot targets: {hits} -> {" ".join(final_state)}')


if __name__ == '__main__':
    main()
