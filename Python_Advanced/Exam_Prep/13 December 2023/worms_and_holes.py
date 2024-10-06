from collections import deque

worms = list(map(int, input().split()))
holes = deque(map(int, input().split()))
worms_qty = len(worms)
holes_qty = len(holes)
matches = 0

while worms and holes:
    current_worm = worms[-1]
    current_hole = holes[0]

    if current_worm == current_hole:
        matches += 1
        holes.popleft()
        worms.pop()
    else:
        current_worm -= 3
        holes.popleft()
        if current_worm <= 0:
            worms.pop()
        else:
            worms[-1] = current_worm


if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and matches == worms_qty:
    print("Every worm found a suitable hole!")
elif not worms and matches != worms_qty:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(map(str, worms))}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(list(map(str, holes)))}")

