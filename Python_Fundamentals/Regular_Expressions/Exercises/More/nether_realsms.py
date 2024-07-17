import re


def get_stats(demons: str):
    demon_book = {}
    for demon in demons.split(','):
        demon = demon.strip()
        health = sum([ord(char) for char in re.findall(r'[^0-9+\-*./]', demon)])
        damage = sum([float(char) for char in re.findall(r'-*\d+[.\d]*', demon)])
        modifiers = re.findall(r'[*/]', demon)
        for modifier in modifiers:
            if modifier == '*':
                damage *= 2
            else:
                damage /= 2
        demon_book[demon] = (health, damage)
    return demon_book


demons = input()

demon_book = get_stats(demons)
for demon, stats in sorted(demon_book.items()):
    print(f'{demon} - {stats[0]} health, {stats[1]:.2f} damage')
