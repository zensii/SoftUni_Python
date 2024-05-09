change = float(input())
coins = [200, 100, 50, 20, 10, 5, 2, 1]


i = 0
total_coins = 0

change = change * 100

while True:
    coin = change // coins[i]
    if coin >= 1:
        total_coins += coin
        change -= coins[i] * coin
        i += 1

    if coin == 0:
        i += 1

    if i > 7:
        break

print(int(total_coins))
