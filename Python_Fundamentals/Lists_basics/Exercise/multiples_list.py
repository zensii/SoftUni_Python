factor = int(input())
count = int(input())
num = factor
lst_numbers = []

while len(lst_numbers) < count:

    if num > 0 and num % factor == 0:
        lst_numbers.append(num)
    num += 1
print(lst_numbers)

