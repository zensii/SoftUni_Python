input_list = [hearts for hearts in map(int, input().split('@'))]
start_position = 0
command = input()
current_position = 0

while command != 'Love!':

    jump = command.split()
    jumps = int(jump[1])

    current_position = current_position + jumps

    if current_position >= len(input_list):
        current_position = start_position

    if input_list[current_position] == 0:
        print(f'Place {current_position} already had Valentine\'s day.')

    else:
        input_list[current_position] -= 2

        if input_list[current_position] == 0:
            print(f'Place {current_position} has Valentine\'s day.')

    command = input()

print(f'Cupid\'s last position was {current_position}.')

if sum(input_list) == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {len([house for house in input_list if house > 0])} places.')