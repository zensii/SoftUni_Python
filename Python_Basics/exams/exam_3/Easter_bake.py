import math

cakes = int(input())

max_sugar = None
max_flour = None
total_sugar = 0
total_flour = 0

for cake in range(cakes):
    sugar = int(input())
    flour = int(input())

    total_sugar += sugar
    total_flour += flour

    if max_flour is None and max_sugar is None:
        max_flour = flour
        max_sugar = sugar

    if sugar > max_sugar:
        max_sugar = sugar

    if flour > max_flour:
        max_flour = flour

sugar_packs = math.ceil(total_sugar/950)
flour_packs = math.ceil(total_flour/750)

print(f'Sugar: {sugar_packs}')
print(f'Flour: {flour_packs}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')

