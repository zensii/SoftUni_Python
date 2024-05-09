budget = float(input())
statists = int(input())
costume_price = float(input())

decor = 0.1 * budget
costume_discount = 0

if statists > 150:
    costume_discount = 0.1

cost = statists * costume_price * (1 - costume_discount) + decor

if cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {cost - budget:.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {budget - cost:.2f} leva left.")
