from math import floor
from math import ceil

X = int(input())  # area land
Y = float(input())  # grapes per sq.m.
Z = int(input())  # wine liter needed
n = int(input())  # personnel

harvest = X * Y
wine_material = harvest * 0.4

wine_liters = wine_material / 2.5

if wine_liters < Z:
    wine_needed = Z - wine_liters
    print(f"It will be a tough winter! More {floor(wine_needed)} liters wine needed.")
else:
    wine_left = wine_liters - Z
    print(f"Good harvest this year! Total wine: {floor(wine_liters)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_left / n)} liters per person.")
