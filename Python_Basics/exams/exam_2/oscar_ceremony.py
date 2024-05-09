hall_price = int(input())

statues_price = hall_price*0.7
catering = statues_price * 0.85
sound = catering/2
total = hall_price + statues_price + catering + sound

print(f'{total:.2f}')
