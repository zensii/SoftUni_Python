budget = float(input())
N = int(input())
M = int(input())
P = int(input())

N_price = 250
M_price = 0.35 * N * N_price
P_price = 0.1 * N * N_price

discount = 0

if N > M:
    discount = 0.15

total_price = (N * N_price + M * M_price + P * P_price) * (1 - discount)

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")

else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
