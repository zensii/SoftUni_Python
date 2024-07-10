num = int(input())
bit_position = int(input())

mask = 1 << bit_position
inverted_mask = ~mask

num = num & inverted_mask

print(num)
