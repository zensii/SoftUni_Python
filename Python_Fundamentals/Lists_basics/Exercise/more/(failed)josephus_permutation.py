solders_order = [int(solder) for solder in input().split()]
k = int(input())
index = 0
eliminated = []
final = ''
while len(solders_order) > 0:

    # NB in order to make a list circular we use the modulo operator!!!

    index = (index + k - 1) % len(solders_order)
    eliminated.append(solders_order.pop(index))

    #  specific formatting was needed

print('[', end='')
for item in range(len(eliminated)-1):
    print(eliminated[item], end=',')
print(eliminated[-1], end='')
print(']')
