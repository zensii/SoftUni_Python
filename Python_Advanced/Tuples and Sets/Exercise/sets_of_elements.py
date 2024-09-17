set_1_length, set_2_length = list(map(int, input().split()))
set_1 = set()
set_2 = set()

for _ in range(set_1_length):
    set_1.add(int(input()))
for _ in range(set_2_length):
    set_2.add(int(input()))

print(*set_1.intersection(set_2), sep='\n')