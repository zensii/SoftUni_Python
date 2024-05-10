flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_box = int(input())
yiest_pk = int(input())

sugar_price = flour_price * 0.75
egg_box_price = flour_price * 1.1
yiest_pk_price = sugar_price * 0.2

total = flour_kg*flour_price+sugar_kg*sugar_price+egg_box*egg_box_price+yiest_pk*yiest_pk_price
print(f'{total:.2f}')

