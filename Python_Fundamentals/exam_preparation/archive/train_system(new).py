def get_old_records():
    """function to get the old records database from the input """
    old_db = {}
    num_of_users = int(input())
    for user in range(num_of_users):
        first_name, last_name, card_num = input().split()
        name = first_name + ' ' + last_name
        old_db.setdefault(name, []).append(card_num)
    return old_db


def get_new_tickets():
    """func to collect the new tickets information from the input
     for later processing"""

    tickets = []

    while True:
        usr_input = input()
        if usr_input == 'time to leave!':
            break
        _, first_name, last_name, destination, card_num = usr_input.split()
        name = first_name + ' ' + last_name
        tickets.append((name, destination, card_num))
    return tickets


def check_existing_card(full_name, card_number, cards_db):

    if full_name in cards_db:
        if card_number in cards_db[full_name]:
            return True
    return False


def update_db(full_name, card_number, database):
    database.setdefault(full_name, []).append(card_number)
    return database


def check_valid_card(card_number):
    digit_sum = sum(int(digit) for digit in card_number)
    if digit_sum % 7 == 0:
        return card_number
    # else:
        # return None


def check_other_owner(card_number, cards_database):
    for cards in cards_database.values():
        if card_number in cards:
            return True
    return False


def get_price(dest, card_number):
    discount = 1
    if card_number:
        discount = 0.5
    price = sum([ord(char) for char in dest]) / 100 * discount

    return price


def issue_ticket(tickets_database, full_name, dest, card_number=None):

    price = get_price(dest, card_number)
    tickets_db.setdefault(full_name, []).append((dest, card_number, price))
    return tickets_db


def print_resutls(tickets_db):

    for customer, tickets_info in sorted_tickets_db.items():
        print(f'{customer}:')
        total = 0
        for ticket in tickets_info:
            dest, card, price = ticket
            total += price
            if card is None:
                card = ''
            else:
                card = f' (using card {card})'
            print(f'--{ticket[0]}: {ticket[-1]:.2f}lv{card}')
        print(f'total: {total:.2f}lv')


def sort_db(tickets_database):

    sorted_db = {k: sorted(v, key=lambda x: x[-1], reverse=True)
            for k, v in sorted(tickets_database.items(),
                key=lambda ticket_nfo: sum(tup[2] for tup in ticket_nfo[1]), reverse=True)}
    return sorted_db


tickets_db = {}
# construct the old db
cards_db = get_old_records()
# get the new tickets info
new_tickets = get_new_tickets()
# process each new ticket
for ticket_info in new_tickets:
    name, destination, card_num = ticket_info

    if check_existing_card(name, card_num, cards_db):
        # issue ticket with discount
        tickets_db = issue_ticket(tickets_db, name, destination, card_num)
    else:
        new_card = check_valid_card(card_num)
        if new_card:  # the card is valid
            if check_other_owner(card_num, cards_db):
                # other owner present - issue ticket without discount
                print(f"card {card_num} already exists for another passenger!")
                tickets_db = issue_ticket(tickets_db, name, destination)
            else:
                #  create new card and update db and issue with discount
                cards_db = update_db(name, card_num, cards_db)
                tickets_db = issue_ticket(tickets_db, name, destination, card_num)
                print(f"issuing card {card_num}")
        else:  # card is not valid
            print(f'card {card_num} is not valid!')
            #  issue ticket without discount
            tickets_db = issue_ticket(tickets_db, name, destination)

sorted_tickets_db = sort_db(tickets_db)
print_resutls(sorted_tickets_db)