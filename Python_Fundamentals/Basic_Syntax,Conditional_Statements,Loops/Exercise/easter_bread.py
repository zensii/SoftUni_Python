budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price / 4
milk_uses = 0
breads = 0
color_eggs = 0

while True:
    price_per_bread = eggs_price + flour_price + milk_price

    if budget - price_per_bread > 0:

        breads += 1
        budget -= price_per_bread
        color_eggs += 3

    else:
        break

    if breads % 3 == 0:
        color_eggs -= breads - 2

print(f'You made {breads} loaves of Easter bread! Now you have {color_eggs} eggs and {budget:.2f}BGN left.')
