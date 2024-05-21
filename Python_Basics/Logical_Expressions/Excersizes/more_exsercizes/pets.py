from math import floor, ceil

days = int(input())
food_left = int(input())
dog_food_day = float(input())
cat_food_day = float(input())
turtle_food_day = float(input()) # in grams

dog_consume = dog_food_day * days
cat_consume = cat_food_day * days
turtle_consume = turtle_food_day * days / 1000

total_food = dog_consume + cat_consume + turtle_consume

if food_left >= total_food:
    leftover = food_left - total_food
    print(f'{floor(leftover)} kilos of food left.')
else:
    more_food_needed = total_food - food_left
    print(f'{ceil(more_food_needed)} more kilos of food are needed.')
