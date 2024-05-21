days = int(input())
room_type = input()
score = input()

nights = days - 1
price = 0

# Prices:
room_for_one_person = 18
apartment = 25
president_apartment = 35

if room_type == 'apartment':
    if nights < 10:
        price = apartment * nights * 0.7
    elif 10 <= nights <= 15:
        price = apartment * nights * 0.65
    else:
        price = apartment * nights * 0.5
elif room_type == 'president apartment':
    if nights < 10:
        price = president_apartment * nights * 0.9
    elif 10 <= nights <= 15:
        price = president_apartment * nights * 0.85
    else:
        price = president_apartment * nights * 0.8
else:
    price = room_for_one_person * nights

if score == 'positive':
    total_price = price * 1.25
else:
    total_price = price * 0.9

print(f'{total_price:.2f}')
