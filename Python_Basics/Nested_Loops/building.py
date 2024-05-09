floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    print()
    for j in range(rooms):
        if i == floors:
            type_room = 'L'
        elif i % 2 == 0:
            type_room = 'O'
        else:
            type_room = 'A'
        print(f'{type_room}{i}{j}', end=' ')
