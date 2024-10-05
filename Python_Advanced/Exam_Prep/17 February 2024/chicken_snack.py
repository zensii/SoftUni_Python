from collections import deque

money = list(map(int, input().split()))
prices = deque(map(int, input().split()))

foods_eaten = 0

while money and prices:
    current_money = money.pop()
    current_price = prices.popleft()

    if current_money >= current_price:
        money_left = current_money - current_price
        if money_left > 0:
            if money:
                money[-1] += money_left
            else:
                money.append(money_left)

        foods_eaten += 1

if foods_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {foods_eaten} foods.")
elif foods_eaten > 1:
    print(f"Henry ate: {foods_eaten} foods.")
elif foods_eaten == 1:
    print(f"Henry ate: {foods_eaten} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")