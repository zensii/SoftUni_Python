
dwarfs_db = {}

while True:
    command = input()

    if command == 'Once upon a time':
        break

    name, hat_color, physics = command.split(' <:> ')
    physics = int(physics)
    if (name, hat_color) not in dwarfs_db:
        dwarfs_db[(name, hat_color)] = physics
    else:
        if dwarfs_db[(name, hat_color)] < physics:
            dwarfs_db[(name, hat_color)] = physics
hat_colors = {}
for dwarf in dwarfs_db.keys():
    hat_colors[dwarf[1]] = hat_colors.get(dwarf[1], 0) + 1

for dwarf, physics in sorted(dwarfs_db.items(), key=lambda x: (-x[1], -hat_colors[x[0][1]])):

    print(f'({dwarf[1]}) {dwarf[0]} <-> {physics}')
