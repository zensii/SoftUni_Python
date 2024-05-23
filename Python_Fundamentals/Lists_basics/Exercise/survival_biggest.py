input_list = input()
n = int(input())
digit_list = []
final_list = []

for num in input_list.split():
    digit_list.append(int(num))

for i in range(n):
    digit_list.remove(min(digit_list))

for num in digit_list:
    final_list.append(str(num))
print(', '.join(final_list))
