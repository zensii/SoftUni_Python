from collections import deque

packages = list(map(int, input().split()))
couriers = deque(map(int, input().split()))

total_delivered_weight = 0

while packages and couriers:
    courier_cap = couriers.popleft()
    pacakge_weight = packages.pop()

    if courier_cap >= pacakge_weight:
        courier_cap -= pacakge_weight * 2
        delivered_weight = pacakge_weight
        if courier_cap > 0:
            couriers.append(courier_cap)
    else:
        pacakge_weight -= courier_cap
        delivered_weight = courier_cap
        packages.append(pacakge_weight)

    total_delivered_weight += delivered_weight

print(f"Total weight: {total_delivered_weight} kg")

if not couriers and not packages:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
else:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")