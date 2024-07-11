def check_validity(ticket):
    if not len(ticket) == 20:
        return False
    return True


def check_jackpot(ticket, symbols):
    for symbol in symbols:
        if ticket == 20 * symbol:
            return f'10{symbol}'
    return False


def check_winner(ticket, symbols):

    left_half = ticket[:len(ticket)//2]
    right_half = ticket[len(ticket)//2:]

    for symbol in symbols:

        if symbol in ticket:
            for combination in range(9, 5, -1):
                if combination * symbol in left_half and combination * symbol in right_half:
                    return f'ticket "{ticket}" - {combination}{symbol}'
    return False


winning_combinations = ['@', '#', '$', '^']
tickets = [ticket.strip() for ticket in input().split(', ')]

for ticket in tickets:
    if check_validity(ticket):
        if check_jackpot(ticket, winning_combinations):
            uninterrupted_length = check_jackpot(ticket, winning_combinations)
            print(f'ticket "{ticket}" - {uninterrupted_length} Jackpot!')
        else:
            if check_winner(ticket, winning_combinations):
                print(check_winner(ticket, winning_combinations))
            else:
                print(f'ticket "{ticket}" - no match')
    else:
        print(f'invalid ticket')
