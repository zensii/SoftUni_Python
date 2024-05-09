groups = int(input())

group_size = 0
Musalah = 0
Montblan = 0
Kilimandjaro = 0
K2 = 0
Everest = 0

for _ in range(groups):
    group_size = int(input())
    if group_size <= 5:
        Musalah += group_size
    elif 6 <= group_size <= 12:
        Montblan += group_size
    elif 13 <= group_size <= 25:
        Kilimandjaro += group_size
    elif 26 <= group_size <= 40:
        K2 += group_size
    else:
        Everest += group_size
total_climbers = Musalah + Montblan + Kilimandjaro + K2 + Everest

print(f'{Musalah/total_climbers*100:.2f}%')
print(f'{Montblan/total_climbers*100:.2f}%')
print(f'{Kilimandjaro/total_climbers*100:.2f}%')
print(f'{K2/total_climbers*100:.2f}%')
print(f'{Everest/total_climbers*100:.2f}%')
