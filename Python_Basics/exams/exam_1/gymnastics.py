country = input()
discipline = input()
difficulty = 0
skill = 0
total_score = 0

if country == 'Russia':
    if discipline == 'ribbon':
        difficulty = 9.100
        skill = 9.4
    elif discipline == 'hoop':
        difficulty = 9.3
        skill = 9.8
    elif discipline == 'rope':
        difficulty = 9.6
        skill = 9
elif country == 'Bulgaria':
    if discipline == 'ribbon':
        difficulty = 9.6
        skill = 9.4
    elif discipline == 'hoop':
        difficulty = 9.55
        skill = 9.75
    elif discipline == 'rope':
        difficulty = 9.5
        skill = 9.4
elif country == 'Italy':
    if discipline == 'ribbon':
        difficulty = 9.2
        skill = 9.5
    elif discipline == 'hoop':
        difficulty = 9.45
        skill = 9.35
    elif discipline == 'rope':
        difficulty = 9.7
        skill = 9.15
total_score = difficulty + skill
print(f'The team of {country} get {total_score:.3f} on {discipline}.')
print(f'{((20 - total_score) / 20) * 100:.2f}%')