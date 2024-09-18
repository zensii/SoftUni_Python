import operator
from collections import deque


def collect_nectar()-> (int,int):

    while nectar and bees[0] > nectar[-1]:
        nectar.pop()
    if nectar:
        return bees.popleft(), nectar.pop()
    else:
        return 0, 0


def prepare_honey(bee:int, nectar:int) -> int:
    honey = 0
    symbol = symbols.popleft()

    if symbol == '*':
        honey = operator.mul(bee, nectar)
    elif symbol == '/':
        if nectar != 0:
            honey = operator.truediv(bee, nectar)
    elif symbol == '+':
        honey = operator.add(bee, nectar)
    elif symbol == '-':
        honey = operator.sub(bee, nectar)

    return honey


bees = deque([int(chars) for chars in input().split()])
nectar = [int(chars) for chars in input().split()]
symbols = deque(input().split())
total_honey = 0

while bees and nectar:

    # step one
    bee, collected_nectar = collect_nectar()

    # step two
    total_honey += abs(prepare_honey(bee, collected_nectar))

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(bee) for bee in bees)}")
elif nectar:
    print(f"Nectar left: {', '.join(str(nectar_uncollected) for nectar_uncollected in nectar)}")


