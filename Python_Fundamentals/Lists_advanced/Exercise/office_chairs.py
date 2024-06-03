rooms = int(input())
free_chairs = 0
insufficient = False
for index, room in enumerate(range(rooms)):
    room_info = input().split()

    if len(room_info[0]) < int(room_info[1]):
        print(f'{int(room_info[1])-len(room_info[0])} more chairs needed in room {index+1}')
        insufficient = True
    else:
        free_chairs += len(room_info[0]) - int(room_info[1])
if not insufficient:
    print(f'Game On, {free_chairs} free chairs left')
