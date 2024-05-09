days = int(input())
hours_per_day = int(input())
price = 0
total_paid = 0

for i in range(1, days+1):
    day_price = 0
    if i % 2 == 0:
        is_even_day = True
    else:
        is_even_day = False

    for j in range(1, hours_per_day+1):
        if j % 2 == 0:
            is_even_hour = True
        else:
            is_even_hour = False

        if (is_even_day and is_even_hour) or (not is_even_day and not is_even_hour):
            price = 1
        elif is_even_day and not is_even_hour:
            price = 2.5
        else:
            price = 1.25

        day_price += price

    print(f'Day: {i} - {day_price:.2f} leva')
    total_paid += day_price

print(f'Total: {total_paid:.2f} leva')
