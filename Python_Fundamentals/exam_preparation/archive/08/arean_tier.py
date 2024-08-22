def collect_gladiators(info, db):

    name, technique, skill = info.split(' -> ')
    skill = int(skill)
    if name not in db:
        db.setdefault(name, {}).update({technique: skill})
    else:
        if technique not in db[name]:
            db[name].update({technique: skill})
        else:
            if skill > db[name][technique]:
                db[name][technique] = skill
    return db


def check_battle_ready(line, db):
    name1, name2 = line.split(' vs ')
    if name1 in db.keys() and name2 in db.keys():
        return set(db[name1].keys()) & set(db[name2].keys())


def check_looser(line, match, db):
    name1, name2 = line.split(' vs ')
    tier = list(match)
    if db[name1][tier[0]] > db[name2][tier[0]]:
        return name2
    return name1


def remove_looser(name, db):
    del db[name]


fighter_db = {}
while True:
    line = input()
    if line == 'Ave Cesar':
        break
    elif '->' in line:
        fighter_db = collect_gladiators(line, fighter_db)

    elif 'vs' in line:
        match = check_battle_ready(line, fighter_db)
        if match:
            looser = check_looser(line, match, fighter_db)
            remove_looser(looser, fighter_db)

ranking = sorted_db = {k: dict(sorted(v.items(), key=lambda x: (-x[1], x[0])))
                       for k, v in sorted(fighter_db.items(), key=lambda x: sum(stats[1]
                                                for stats in x[1].items()), reverse=True)}

for gladiator, stats in ranking.items():
    total_skill = sum(skill[1] for skill in stats.items())
    print(f'{gladiator}: {total_skill} skill')
    for technique, skill in stats.items():
        print(f'- {technique} <!> {skill}')
