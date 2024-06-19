def collect_dragons(number):
    dragons_db = {}
    colors = {}
    for i in range(number):

        color, name, damage, health, armor = input().split()

        if damage == 'null':
            damage = 45
        if health == 'null':
            health = 250
        if armor == 'null':
            armor = 10

        damage = int(damage)
        health = int(health)
        armor = int(armor)
        stats = {'damage': damage, 'health': health, 'armor': armor}

        if not (color, name) in dragons_db.keys():
            colors = collect_colors(color, colors)

        dragons_db[(color, name)] = stats

    return dragons_db, colors


def summed_stats(colors, dragons_db):
    sum_per_color = {color: {'damage': 0, 'health': 0, 'armor': 0} for color in colors}

    for color in colors:
        for dragon, stats in dragons_db.items():
            if dragon[0] == color:
                sum_per_color[color]['damage'] += stats['damage']
                sum_per_color[color]['health'] += stats['health']
                sum_per_color[color]['armor'] += stats['armor']
    return sum_per_color


def collect_colors(color, colors):
    colors[color] = colors.get(color, 0) + 1
    return colors


def main():
    number = int(input())

    dragons_db, colors = collect_dragons(number)

    for color in colors:
        number_of_dragons = colors[color]
        sum_per_color = summed_stats(colors, dragons_db)
        damage = sum_per_color[color]['damage']
        health = sum_per_color[color]['health']
        armor = sum_per_color[color]['armor']
        print(f'{color}::({damage/number_of_dragons:.2f}/{health/number_of_dragons:.2f}/{armor/number_of_dragons:.2f})')

        for color_name, stats in sorted(dragons_db.items(), key=lambda x: x[0][1]):
            if color_name[0] == color:
                print(f"-{color_name[1]} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")


if __name__ == '__main__':
    main()
