planned_gifts = input().split()
final_list = []
command = input()
while command != 'No Money':

    command = command.split()

    if command[0] == 'OutOfStock':

        while command[1] in planned_gifts:
            planned_gifts[planned_gifts.index(command[1])] = 'None'

    if command[0] == 'Required' and 0 <= int(command[2]) < len(planned_gifts):  # here it was critical to add the check
        planned_gifts[int(command[2])] = command[1]                             # if the index command[0] is also larger
                                                                                # than 0
    if command[0] == 'JustInCase':

        planned_gifts[-1] = command[1]

    command = input()

for item in planned_gifts:
    if item != 'None':
        final_list.append(item)


print(' '.join(final_list))
