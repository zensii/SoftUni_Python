width = int(input())
length = int(input())
height = int(input())
entry = input()
volume = width * length * height

while volume > 0:
    if entry != 'Done':
        boxes = int(entry)
        volume -= boxes
    else:
        print(f'{volume} Cubic meters left.')
        break
    if volume < 0:
        print(f'No more free space! You need {abs(volume)} Cubic meters more.')
        break
    entry = input()
