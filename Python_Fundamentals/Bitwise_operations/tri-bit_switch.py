n = int(input())
position = int(input())
mask = 7

shifted_mask = mask << position

result = n ^ shifted_mask

print(result)