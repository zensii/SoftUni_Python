vacation = float(input())
puzzle_pcs = int(input())
doll_pcs = int(input())
bear_pcs = int(input())
minion_pcs = int(input())
truck_pcs = int(input())

puzzle = 2.6
doll = 3
bear = 4.1
minion = 8.2
truck = 2
discount = 0
rent = 0.1

total = (puzzle_pcs * puzzle + doll * doll_pcs + bear * bear_pcs + minion * minion_pcs + truck * truck_pcs)

if puzzle_pcs + doll_pcs + bear_pcs + minion_pcs + truck_pcs >= 50:
    discount = 0.25
    total = total * (1 - discount)

total = total * (1 - rent)

if total >= vacation:
    print(f"Yes! {total - vacation:.2f} lv left.")
else:
    print(f"Not enough money! {abs(total - vacation):.2f} lv needed.")
