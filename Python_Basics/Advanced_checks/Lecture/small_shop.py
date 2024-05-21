item = input()
city = input()
quantity = float(input())

price = 0

if item == "coffee":
    if city == "Sofia":
        price = 0.5
        print(price * quantity)
    elif city == "Plovdiv":
        price = 0.4
        print(price * quantity)
    elif city == "Varna":
        price = 0.45
        print(price * quantity)

elif item == "water":
    if city == "Sofia":
        price = 0.8
        print(price * quantity)
    elif city == "Plovdiv":
        price = 0.7
        print(price * quantity)
    elif city == "Varna":
        price = 0.7
        print(price * quantity)

elif item == "sweets":
    if city == "Sofia":
        price = 1.45
        print(price * quantity)
    elif city == "Plovdiv":
        price = 1.3
        print(price * quantity)
    elif city == "Varna":
        price = 1.35
        print(price * quantity)

elif item == "peanuts":
    if city == "Sofia":
        price = 1.6
        print(price * quantity)
    elif city == "Plovdiv":
        price = 1.5
        print(price * quantity)
    elif city == "Varna":
        price = 1.55
        print(price * quantity)

elif item == "beer":
    if city == "Sofia":
        price = 1.2
        print(price * quantity)
    elif city == "Plovdiv":
        price = 1.15
        print(price * quantity)
    elif city == "Varna":
        price = 1.1
        print(price * quantity)
