from collections import deque

bullet_price = int(input())
full_barrel_size = int(input())
bullets = deque(map(int, input().split()))
locks = deque(map(int, input().split()))
pay = int(input())

cost = 0
barrel_size = full_barrel_size

while locks and bullets:

    current_bullet = bullets.pop()
    cost += bullet_price
    barrel_size -= 1
    current_lock = locks[0]

    if current_bullet <= current_lock:
        locks.popleft()
        print('Bang!')
    else:
        print('Ping!')

    if barrel_size == 0 and bullets:
        print('Reloading!')
        barrel_size = full_barrel_size

if not locks:
    print(f'{len(bullets)} bullets left. Earned ${pay - cost}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")