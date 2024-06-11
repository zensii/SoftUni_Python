def urgent(item, list):

    if item not in list:
        list.insert(0, item)


def unnecessary(item, list):

    while item in list:
        list.remove(item)


def correct(old_item, new_item, list):

    while old_item in list:
        list[list.index(old_item)] = new_item


def rearrange(item, list):

    if item in list and list.index(item) < len(list)-1-list.count(item):
        list.remove(item)
        list.append(item)


def main():
    initial_list = input().split('!')
    command = input()

    while True:

        action = command.split()

        if action[0] == 'Go':
            print(', '.join(initial_list))
            break
        elif action[0] == 'Urgent':
            urgent(action[1], initial_list)
        elif action[0] == 'Unnecessary':
            unnecessary(action[1], initial_list)
        elif action[0] == 'Correct':
            correct(action[1], action[2], initial_list)
        elif action[0] == 'Rearrange':
            rearrange(action[1], initial_list)

        command = input()


if __name__ == "__main__":
    main()
