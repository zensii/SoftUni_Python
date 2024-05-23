n = int(input())
numbers=[]
filtered_lst = []

for entry in range(n):
    numbers.append(int(input()))
command = input()

if command == 'even':
    for num in numbers:
        if num % 2 == 0 or num == 0:
            filtered_lst.append(num)

elif command == 'odd':
    for num in numbers:
        if num % 2 != 0:
            filtered_lst.append(num)

elif command == 'negative':
    for num in numbers:
        if num < 0:
            filtered_lst.append(num)

elif command == 'positive':
    for num in numbers :
        if num >= 0:
            filtered_lst.append(num)

print(filtered_lst)
