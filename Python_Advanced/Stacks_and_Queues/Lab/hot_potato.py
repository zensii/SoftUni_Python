names = input().split()
counter = int(input())
position = 0
while len(names) > 1:
    position = (position + counter - 1)  % len(names)
    print(f'Removed {names.pop(position)}')

print(f'Last is {names[0]}')