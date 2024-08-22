def collect_old_cards(n: int):
    old_cards = {}
    for _ in range(num_cards):
        first_name, last_name, ticket_num = input().split()
        full_name = first_name + ' ' + last_name
        old_cards.setdefault(full_name, []).append(ticket_num)
    return old_cards


def collect_commands():
    commands = []
    while True:
        usr_input = input()
        if usr_input == 'time to leave!':
            break
        command = usr_input
        commands.append(command)
    return commands


# def check_existing(full_name, card_number, tickets, old_cards):
#
#     if ((any(card_number in cards['card'] for person, info in tickets.items() for cards in info if person != full_name))
#             or (any(card_number in cards for person, cards in old_cards.items() if person != full_name))):
#         print(f"card {card_number} already exists for another passenger!")
#
#         return True

def check_existing(full_name, card_number, tickets, old_cards):
    in_tickets = any(
        card_number in cards['card'] for person, info in tickets.items() for cards in info if person != full_name)
    in_old_cards = any(card_number in cards for person, cards in old_cards.items() if person != full_name)

    if in_tickets or in_old_cards:
        print(f"card {card_number} already exists for another passenger!")
        return True
    return False


def update_tickets(full_name, destination, tickets, discount, card_number='invalid'):

    price = sum(ord(character) for character in destination) / 100 * discount

    if full_name not in tickets:
        tickets[full_name] = [{'destination': destination, 'card': card_number, 'price': price}]
    else:
        tickets[full_name].append({'destination': destination, 'card': card_number, 'price': price})

    return tickets


def check_valid_card(card_number):

    if sum(int(digit) for digit in card_number) % 7 != 0:
        print(f"card {card_number} is not valid!")
        return False
    return True


def process_commands(commands, old_cards):
    tickets = {}
    for command in commands:

        discount = 1

        _, first_name, last_name, destination, card_number = command.split()
        full_name = first_name + ' ' + last_name

        if full_name in old_cards and card_number in old_cards[full_name]:
            discount = 0.5
            tickets = update_tickets(full_name, destination, tickets, discount, card_number)

        else:
            if not check_valid_card(card_number):
                tickets = update_tickets(full_name, destination, tickets, discount)
            else:
                if check_existing(full_name, card_number, tickets, old_cards):
                    tickets = update_tickets(full_name, destination, tickets, discount)
                else:
                    print(f"issuing card {card_number}")
                    discount = 0.5
                    tickets = update_tickets(full_name, destination, tickets, discount, card_number)

    return tickets


num_cards = int(input())
old_cards = collect_old_cards(num_cards)
commands = collect_commands()
tickets = process_commands(commands, old_cards)

for person in tickets:
    tickets[person] = sorted(tickets[person], key=lambda x: x['price'], reverse=True)

sorted_dict = dict(sorted(tickets.items(), key=lambda x: sum(ticket['price'] for ticket in x[1]), reverse=True))

for person, tickets in sorted_dict.items():
    total_price = sum(ticket['price'] for ticket in tickets)
    print(f"{person}:")
    for ticket in tickets:
        card_info = ''
        if ticket['card'] != 'invalid':
            card_info = f" (using card {ticket['card']})"
        print(f"--{ticket['destination']}: {ticket['price']:.2f}lv" + card_info)
    print(f"total: {total_price:.2f}lv")
