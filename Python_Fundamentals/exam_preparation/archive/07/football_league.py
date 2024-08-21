import re


def get_code(code):
    reg_code = ''

    for char in code:
        if char.isalnum():
            reg_code += char
        else:
            reg_code += ('\\' + char)

    return reg_code


def match_result(code, usr_input):

    pattern = f'{reg_code}([a-zA-Z]*){reg_code}'
    score_pattern = r'(\d+):(\d+)'

    teams = [team[::-1].upper() for team in re.findall(pattern, usr_input)]
    [match_score] = re.findall(score_pattern, usr_input)

    result = list(zip(teams, list(match_score)))

    return result



def update_leaderboard(match_result, leaderboard):
    winner = None

    first_team, first_score = match_result[0]
    second_team, second_score = match_result[1]
    first_score, second_score = int(first_score), int(second_score)
    if first_score != second_score:
        winner = max(match_result, key=lambda x: int(x[1]))[0]

    leaderboard.setdefault(first_team, {'points': 0, 'goals': 0})['goals'] += first_score
    leaderboard.setdefault(second_team, {'points': 0, 'goals': 0})['goals'] += second_score

    if winner is None:
        leaderboard[first_team]['points'] += 1
        leaderboard[second_team]['points'] += 1
    else:
        leaderboard[winner]['points'] += 3

    return leaderboard


def sort_leaderboard(leaderboard):
    return dict(sorted(leaderboard.items(), key=lambda x: (-x[1]['points'], x)))


def sort_by_goal(leaderboard):
    return dict(sorted(leaderboard.items(), key=lambda x: (-x[1]['goals'], x)))



reg_code = get_code(input())
leaderboard = {}
while True:

    usr_input = input()

    if usr_input == 'final':
        break

    match_results = match_result(reg_code, usr_input)
    leaderboard = update_leaderboard(match_results, leaderboard)

sorted_lb = sort_leaderboard(leaderboard)
position = 1
print('League standings:')
for k, v in sorted_lb.items():
    print(f"{position}. {k} {v['points']}")
    position += 1
print('Top 3 scored goals:')
sorted_goals = sort_by_goal(leaderboard)

for k, v in list(sorted_goals.items())[:3]:
    print(f"- {k} -> {v['goals']}")
