round_of_championship = input()
ticket_type = input()
number_of_tickets = int(input())
picture_trophy = input()
ticket_price = 0
base_price = 0
discount = 1
free_photo = False
total_price = 0

if round_of_championship == 'Quarter final':
    if ticket_type == 'Standard':
        ticket_price = 55.5
    elif ticket_type == 'Premium':
        ticket_price = 105.2
    else:
        ticket_price = 118.9
elif round_of_championship == 'Semi final':
    if ticket_type == 'Standard':
        ticket_price = 77.88
    elif ticket_type == 'Premium':
        ticket_price = 125.22
    else:
        ticket_price = 300.4
else:
    if ticket_type == 'Standard':
        ticket_price = 110.1
    elif ticket_type == 'Premium':
        ticket_price = 160.66
    else:
        ticket_price = 400

base_price = ticket_price * number_of_tickets

if base_price > 4000:
    discount = 0.75
    free_photo = True

elif base_price > 2500:
    discount = 0.9

if picture_trophy == 'Y':
    if free_photo:
        total_price = base_price * discount
    else:
        total_price = base_price * discount + 40 * number_of_tickets
else:
    total_price = base_price * discount

print(f'{total_price:.2f}')
