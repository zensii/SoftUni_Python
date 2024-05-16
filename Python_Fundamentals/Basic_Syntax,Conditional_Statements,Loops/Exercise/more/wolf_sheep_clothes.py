queue = input()

herd = list(queue.split(', '))
reversed_herd = herd[::-1]

for index in range(len(reversed_herd)):

    if reversed_herd[index] == 'wolf':
        if index == 0:
            print('Please go away and stop eating my sheep')
        else:
            print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')
        break
