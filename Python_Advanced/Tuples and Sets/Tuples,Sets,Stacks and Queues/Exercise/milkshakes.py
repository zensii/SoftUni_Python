from collections import deque

milkshakes = 0
chocolates = [int(char) for char in input().split(', ')]
cups_milk = deque([int(char) for char in input().split(', ')])

while chocolates and cups_milk and milkshakes < 5:

    while chocolates and chocolates[-1] <= 0:
        chocolates.pop()
    while cups_milk and cups_milk[0] <= 0:
        cups_milk.popleft()

    if chocolates and cups_milk:
        if chocolates[-1] == cups_milk[0]:
            milkshakes += 1
            chocolates.pop()
            cups_milk.popleft()
        else:
            chocolates[-1] -= 5
            cups_milk.append(cups_milk.popleft())

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(dig) for dig in chocolates)}")
else:
    print("Chocolate: empty")
if cups_milk:
    print(f"Milk: {', '.join(str(dig) for dig in cups_milk)}")
else:
    print("Milk: empty")
