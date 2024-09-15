container = [int(x) for x in input().split()]
capacity = int(input())
hangers = 1
hang = 0

while container:
    if hang + container[-1] <= capacity:
        hang += container.pop()
    else:
        hangers += 1
        hang = container.pop()

print(hangers)
