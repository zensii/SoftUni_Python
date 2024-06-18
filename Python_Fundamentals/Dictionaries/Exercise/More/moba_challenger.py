def split_command(command):
    player_name, position, skill = command.split(' -> ')
    skill = int(skill)
    return player_name, position, skill


def add_player(player_name, position, skill, ranking):
    position_power = {position: skill}
    if player_name not in ranking.keys():

        ranking[player_name] = position_power
    else:
        if position not in ranking[player_name].keys():
            ranking[player_name].update(position_power)
        else:
            if ranking[player_name][position] < skill:
                ranking[player_name][position] = skill
    return ranking


def check_equal_positions(player_1, player_2, ranking):
    player_1_positions = list(ranking[player_1].keys())
    player_2_positions = list(ranking[player_2].keys())
    for position in player_1_positions:
        if position in player_2_positions:
            if ranking[player_1][position] == ranking[player_2][position]:
                return False
            return True
    return False


def compare_total_skill(name_1, name_2, ranking):
    if sum(ranking[name_1].values()) > sum(ranking[name_2].values()):
        return name_2
    else:
        return name_1


def check_if_pvp_possible(player_one, player_two, ranking):

    if player_one in ranking.keys() and player_two in ranking.keys():
        if check_equal_positions(player_one, player_two, ranking):
            return True
    return False


def calculate_totals(ranking):
    totals = {player: sum(ranking[player].values()) for player in ranking.keys()}
    return totals


def main():
    command = input()
    ranking = {}
    while command != 'Season end':

        if 'vs' in command:
            player_one, player_two = command.split(' vs ')

            if check_if_pvp_possible(player_one, player_two, ranking):
                looser = compare_total_skill(player_one, player_two, ranking)
                del ranking[looser]

        else:
            player_name, position, skill = split_command(command)
            ranking = add_player(player_name, position, skill, ranking)

        command = input()

    totals = calculate_totals(ranking)
    for player, score in sorted(totals.items(), key=lambda item: (-item[1], item[0])):
        print(f'{player}: {score} skill')
        for position, skill in sorted(ranking[player].items(), key=lambda item: (-item[1], item[0])):
            print(f'- {position} <::> {skill}')


if __name__ == "__main__":
    main()
