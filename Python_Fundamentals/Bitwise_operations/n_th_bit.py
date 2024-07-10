num = int(input())
position = int(input())

bit_position_1 = (num >> position) & 1

print(bit_position_1)
