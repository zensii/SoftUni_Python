number_inputs = int(input())
capacity = 0

for inputs in range(number_inputs):
    add_water = int(input())
    capacity += add_water
    if capacity > 255:
        capacity -= add_water
        print(f'Insufficient capacity!')
        continue
print(capacity)
