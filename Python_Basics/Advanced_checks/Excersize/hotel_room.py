month = input()
nights = int(input())

total_price_ap = 0
total_price_stu = 0
price_ap = 0
price_stu = 0
discount_ap = 0
discount_stu = 0

if month == 'May' or month == 'October':
    price_stu = 50
    price_ap = 65
    if 7 < nights <= 14:
        discount_stu = 0.05
    elif nights > 14:
        discount_stu = 0.3
        discount_ap = 0.1

elif month == 'June' or month == 'September':
    price_stu = 75.20
    price_ap = 68.70
    if nights > 14:
        discount_stu = 0.2
        discount_ap = 0.1
else:
    price_stu = 76
    price_ap = 77
    if nights > 14:
        discount_ap = 0.1

total_price_ap = nights * (price_ap * (1 - discount_ap))
total_price_stu = nights * (price_stu * (1 - discount_stu))

print(f'Apartment: {total_price_ap:.2f} lv.')
print(f'Studio: {total_price_stu:.2f} lv.')
