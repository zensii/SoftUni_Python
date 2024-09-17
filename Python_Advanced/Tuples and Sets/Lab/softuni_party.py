num_guests = int(input())
reservations = set()

for reservation in range(num_guests):
    reservations.add(input())

while True:
    guest = input()
    if guest == 'END':
        break
    else:
        reservations.remove(guest)

print(len(reservations))

print(*sorted(list(reservations), key=lambda x: (-x[0].isdigit(), x[0])), sep='\n')
