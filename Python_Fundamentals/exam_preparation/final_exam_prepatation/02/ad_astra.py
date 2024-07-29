import re

regex = r'([|#])([A-Za-z ]+)\1(\d\d\/\d\d\/\d\d)\1([0-9]+)\1'
string = input()

foods = [food for food in re.findall(regex, string)]

total_calories = sum(int(calories[3]) for calories in foods)

print(f'You have food to last you for: {total_calories//2000} days!')
for food in foods:
    print(f'Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[3]}')
