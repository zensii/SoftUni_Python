age = int(input())
price = float(input())
toy_price = int(input())

toys = 0
money = 0
coef = 0
total = 0

for year in range(1, age+1):
    if year % 2 == 0:
        coef += 1
        money += (coef * 10) - 1
    else:
        toys += 1

total = money + toys * toy_price

if total >= price:
    print(f'Yes! {total - price:.2f}')
else:
    print(f'No! {price - total:.2f}')
