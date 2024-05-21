hrizantemi = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

price_hrizantemi = 0
price_roses = 0
price_tulips = 0
total_price = 0
discount = 0
extra = 1.15

if season == 'Spring' or season == 'Summer':
    price_roses = 4.1
    price_tulips = 2.5
    price_hrizantemi = 2
else:
    price_roses = 4.5
    price_tulips = 4.15
    price_hrizantemi = 3.75

total_price = hrizantemi * price_hrizantemi + roses * price_roses + tulips * price_tulips

if holiday == 'Y':
    total_price = total_price * extra

if tulips > 7 and season == 'Spring':
    total_price = total_price * 0.95
if roses >= 10 and season == 'Winter':
    total_price = total_price * 0.9
if roses + hrizantemi + tulips > 20:
    total_price = total_price * 0.8

print(f'{total_price + 2:.2f}')
