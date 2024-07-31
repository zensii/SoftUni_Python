def collect_hero_stats(n):
    heroes = {}
    for hero in range(n):
        hero_name, hp, mp = input().split()
        hp, mp = int(hp), int(mp)
        if hp > 100:
            hp = 100
        if mp > 200:
            mp = 200
        heroes[hero_name] = {'HP': hp, 'MP': mp}

    return heroes


def cast(hero_info, heroes):
    hero_name, mp_needed, spell = hero_info[0], int(hero_info[1]), hero_info[2]
    if heroes[hero_name]['MP'] >= mp_needed:
        heroes[hero_name]['MP'] -= mp_needed
        print(f"{hero_name} has successfully cast {spell} and now has {heroes[hero_name]['MP']} MP!")
    else:
        print(f'{hero_name} does not have enough MP to cast {spell}!')
    return heroes


def takedmg(hero_info, heroes):
    hero_name, damage, attacker = hero_info[0], int(hero_info[1]), hero_info[2]
    if heroes[hero_name]['HP'] - damage <= 0:
        del heroes[hero_name]
        print(f'{hero_name} has been killed by {attacker}!')
    else:
        heroes[hero_name]['HP'] -= damage
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
    return heroes


def recharge(hero_info, heroes):
    hero_name, amount = hero_info[0], int(hero_info[1])
    if heroes[hero_name]['MP'] + amount <= 200:
        heroes[hero_name]['MP'] += amount
        amount_increased = amount
    else:
        amount_increased = 200 - heroes[hero_name]['MP']
        heroes[hero_name]['MP'] = 200
    print(f'{hero_name} recharged for {amount_increased} MP!')
    return heroes


def heal(hero_info, heroes):
    hero_name, amount = hero_info[0], int(hero_info[1])
    if heroes[hero_name]['HP'] + amount <= 100:
        heroes[hero_name]['HP'] += amount
        amount_increased = amount
    else:
        amount_increased = 100 - heroes[hero_name]['HP']
        heroes[hero_name]['HP'] = 100
    print(f'{hero_name} healed for {amount_increased} HP!')
    return heroes


def process_cmd(cmd: list, heroes):
    for command in commands:
        action, *hero_info = command.split(' - ')
        if action == 'CastSpell':
            heroes = cast(hero_info, heroes)
        elif action == 'TakeDamage':
            heroes = takedmg(hero_info, heroes)
        elif action == 'Recharge':
            heroes = recharge(hero_info, heroes)
        elif action == 'Heal':
            heroes = heal(hero_info, heroes)

    return heroes


num_heroes = int(input())
heroes = collect_hero_stats(num_heroes)
commands = []
while True:
    command = input()
    if command == 'End':
        break
    commands.append(command)
heroes = process_cmd(commands, heroes)

for hero, stats in heroes.items():
    print(hero)
    print(f"  HP: {stats['HP']}")
    print(f"  MP: {stats['MP']}")
