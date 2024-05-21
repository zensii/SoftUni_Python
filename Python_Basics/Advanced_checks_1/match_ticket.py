budget = float(input())
category = input()
people = int(input())

VIP = 499.99
Normal = 249.99
ticket_cost = 0
travel_cost = 0
ticket_budget = 0

if 1 <= people <= 4:
    travel_cost = 0.75
elif 5 <= people <= 9:
    travel_cost = 0.6
elif 10 <= people <= 24:
    travel_cost = 0.5
elif 25 <= people <= 49:
    travel_cost = 0.4
elif people >= 50:
    travel_cost = 0.25

travel_cost = travel_cost * budget

if category == 'VIP':
    ticket_cost = people * VIP
    if travel_cost + ticket_cost <= budget:
        print(f'Yes! You have {budget - travel_cost - ticket_cost:.2f} leva left.')
    else:
        print(f'Not enough money! You need {travel_cost + ticket_cost - budget:.2f} leva.')
elif category == 'Normal':
    ticket_cost = people * Normal
    if travel_cost + ticket_cost <= budget:
        print(f'Yes! You have {budget - travel_cost - ticket_cost:.2f} leva left.')
    else:
        print(f'Not enough money! You need {travel_cost + ticket_cost - budget:.2f} leva.')
