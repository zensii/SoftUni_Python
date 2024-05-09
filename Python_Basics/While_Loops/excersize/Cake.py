length = int(input())
width = int(input())

pieces = 0
total_pieces = length * width

while True:
    entry = input()
    if entry != 'STOP':
        taken_pieces = int(entry)
        total_pieces -= taken_pieces
        if total_pieces < 0:
            print(f'No more cake left! You need {abs(total_pieces)} pieces more.')
            break
    else:
        if total_pieces >= 0:
            print(f'{total_pieces} pieces are left.')
            break
