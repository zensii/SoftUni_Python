from collections import deque

contestants = deque(list(map(int, input().split())))
pies = list(map(int, input().split()))

while contestants and pies:
    current_contestant = contestants.popleft()
    current_pie = pies.pop()

    if current_pie <= current_contestant:
        current_contestant -= current_pie
        if current_contestant:
            contestants.append(current_contestant)
    else:
        current_pie -= current_contestant

        if current_pie == 1 and pies:
            pies[-1] += current_pie
        elif current_pie > 0:
            pies.append(current_pie)

if not pies and not contestants:
    print("We have a champion!")
elif not pies:
    print("We will have to wait for more pies to be baked!")
    print("Contestants left:", ', '.join(map(str, contestants)))
elif not contestants:
    print("Our contestants need to rest!")
    print("Pies left:", ', '.join(map(str, pies)))