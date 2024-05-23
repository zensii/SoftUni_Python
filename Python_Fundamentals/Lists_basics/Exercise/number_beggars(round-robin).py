string_coins = input().split(', ')
beggars = int(input())
beggar_earnings = [0] * beggars

for index, coin in enumerate(string_coins):
    beggar_index = index % beggars
    beggar_earnings[beggar_index] += int(coin)

print(beggar_earnings)
