start = int(input())
end = int(input())
magic_number = int(input())
combination = 0
stop = False

for i in range(start, end+1):
    for j in range(start, end+1):
        combination += 1
        if i + j == magic_number:
            print(f'Combination N:{combination} ({i} + {j} = {magic_number})')
            stop = True
            break
    if stop:
        break
else:
    print(f'{combination} combinations - neither equals {magic_number}')
