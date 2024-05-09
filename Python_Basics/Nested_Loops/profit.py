one_lev = int(input())
two_lev = int(input())
five_lev = int(input())
amount = int(input())

for coin_1 in range(0, one_lev+1):
    for coin_2 in range(0, two_lev+1):
        for bill_5 in range(0, five_lev + 1):
            if coin_1 + coin_2*2 + bill_5*5 == amount:
                print(f'{coin_1} * 1 lv. + {coin_2} * 2 lv. + {bill_5} * 5 lv. = {amount} lv.')
                