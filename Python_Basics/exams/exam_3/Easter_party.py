guests = int(input())
price_person = float(input())
budget = float(input())
discount = 0
cake_price = budget * 0.1
total_cost = 0

if 10 <= guests <= 15:
    discount = 0.15
elif 15 < guests <= 20:
    discount = 0.2
elif guests > 20:
    discount = 0.25

total_cost = guests * (price_person * (1 - discount)) + cake_price

if budget >= total_cost:
    print(f'It is party time! {budget - total_cost:.2f} leva left.')
else:
    print(f'No party! {abs(budget - total_cost):.2f} leva needed.')
