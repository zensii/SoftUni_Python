n = int(input())
intersections = []

for _ in range(n):
    range_one, range_two = input().split('-')
    set_1 = {num for num in range(int(range_one.split(',')[0]),int(range_one.split(',')[1]) + 1)}
    set_2 = {num for num in range(int(range_two.split(',')[0]),int(range_two.split(',')[1]) + 1)}
    intersection = set_1.intersection(set_2)
    intersections.append(list(intersection))

longest = sorted(intersections, key=len)[-1]
print(f"Longest intersection is {longest} with length {len(longest)}")