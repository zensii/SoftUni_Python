from collections import deque

cups: deque[int] = deque(map(int, input().split()))
bottles: list[int] = list(map(int, input().split()))

wasted_water: int = 0

while cups and bottles:
    current_bottle = bottles.pop()

    if current_bottle >= cups[0]:
        wasted_water += current_bottle - cups.popleft()
    else:
        cups[0] -= current_bottle

if cups and not bottles:
    print("Cups:",*cups, sep=' ')
else:
    print("Bottles:", *bottles, sep=' ')

print(f'Wasted litters of water: {wasted_water}')