n = int(input())
parked = set()

for _ in range(n):
    direction, plate = input().split(', ')
    if direction == 'IN':
        parked.add(plate)
    else:
        parked.remove(plate)

if parked:
    for plate in parked:
        print(plate)
else:
    print('Parking Lot is Empty')
