season = input()
group = input()
students = int(input())
nights = int(input())

sport = ''
total_price = 0
price = 0
discount = 0

if season == 'Winter':
    if group == 'girls':
        price = 9.6
        sport = 'Gymnastics'
    elif group == 'boys':
        sport = 'Judo'
        price = 9.6
    else:
        price = 10
        sport = 'ski'
elif season == 'Spring':
    if group == 'girls':
        price = 7.2
        sport = 'Athletics'
    elif group == 'boys':
        price = 7.2
        sport = 'Tennis'
    else:
        price = 9.5
        sport = 'Cycling'
else:
    if group == 'girls':
        price = 15
        sport = 'Volleyball'
    elif group == 'boys':
        price = 15
        sport = 'Football'
    else:
        sport = 'Swimming'
        price = 20

if students >= 50:
    discount = 0.5
elif 20 <= students < 50:
    discount = 0.15
elif 10 <= students < 20:
    discount = 0.05

total_price = students * nights * price * (1 - discount)

print(f'{sport} {total_price:.2f} lv.')
