string_of_coins = input().split(', ')
beggars = list(range(int(input())))
money = [0] * len(beggars)

for index in range(0, len(string_of_coins), len(beggars)):
    for beggar in beggars:
        if index+beggar < len(string_of_coins):
            money[beggar] += int(string_of_coins[index+beggar])

print(money)