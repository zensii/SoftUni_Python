France_price = [30, 35, 40]
Italy_price = [28, 32, 39]
Germany_price = [32, 37, 43]


destination_option = input()
date = input()
nights = int(input())


price = 0
cost = 0
index = None

if date == '21-23':
    index = 0
elif date == '24-27':
    index = 1
elif date == '28-31':
    index = 2

if destination_option == 'France':
    price = France_price[index]
elif destination_option == 'Italy':
    price = Italy_price[index]
elif destination_option == 'Germany':
    price = Germany_price[index]

cost = price * nights

print(f'Easter trip to {destination_option} : {cost:.2f} leva.')
