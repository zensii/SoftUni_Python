from collections import deque

food = int(input())
customers = deque(map(int, input().split()))
max_order = max(customers)

for customer in customers.copy():
    if customer <= food:
        food -= customer
        customers.popleft()
    else:
        break

print(max_order)
print("Orders complete" if not customers else f"Orders left: {' '.join([str(customer) for customer in customers])}")
