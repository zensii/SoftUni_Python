from collections import deque


def fight(defenders, attackers):

    if defenders >= 7 and attackers >= 1:
        defenders -= 7
        attackers -= 1

    elif defenders < 7 and attackers >= 1:
        defenders = 0

    return defenders, attackers

bees = deque(list(map(int, input().split())))
bee_eaters = list(map(int, input().split()))

while bees and bee_eaters:
    defenders = bees.popleft()
    attackers = bee_eaters.pop()

    while defenders and attackers:
        defenders, attackers = fight(defenders, attackers)

    if defenders:
        bees.append(defenders)
    elif attackers:
        bee_eaters.append(attackers)

print("The final battle is over!")
if bees:
    print(f"Bee groups left: {', '.join(list(map(str, bees)))}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(list(map(str, bee_eaters)))}")
else:
    print("But no one made it out alive!")