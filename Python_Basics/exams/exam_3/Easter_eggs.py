total_eggs = int(input())

colors = {'red': 0, 'orange': 0, 'blue': 0, 'green': 0}

for egg in range(total_eggs):
    color = input()
    colors[color] += 1

for color, number in colors.items():
    print(f'{color.capitalize()} eggs: {number}')

print(f'Max eggs: {max(colors.values())} -> {max(colors, key=colors.get)}')


