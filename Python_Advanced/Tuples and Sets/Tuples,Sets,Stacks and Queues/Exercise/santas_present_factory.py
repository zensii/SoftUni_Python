from collections import deque
from collections import Counter

recipes = {
    'Doll': 150,
    'Wooden train': 250,
    'Teddy bear': 300,
    'Bicycle': 400
}

crafted_presents = Counter()

materials = [int(mat) for mat in input().split()]
magic_level = deque([int(magic) for magic in input().split()])

while materials and magic_level:

    result = materials[-1] * magic_level[0]

    if result in recipes.values():
        present = [present for present, value in recipes.items() if value == result][0]
        crafted_presents[present] = crafted_presents.get(present, 0) + 1
        materials.pop()
        magic_level.popleft()

    else:
        if result < 0:
            materials.append(materials.pop() + magic_level.popleft())

        elif result > 0:
            magic_level.popleft()
            materials[-1] += 15

        else:
            if materials[-1] == 0:
                materials.pop()
            if magic_level[0] == 0:
                magic_level.popleft()


if (('Doll' in crafted_presents and 'Train' in crafted_presents)
        or ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents)):

    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(mat) for mat in reversed(materials))}")
if magic_level:
    print(f"Magic left: {', '.join(str(magic) for magic in magic_level)}")

print(*[f"{key}: {value}" for key, value in sorted(crafted_presents.items())], sep='\n')