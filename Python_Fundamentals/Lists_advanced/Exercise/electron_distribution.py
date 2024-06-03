number_electrons = int(input())
shell = 1
final_list = []

while number_electrons >= 2*shell**2:
    final_list.append(2*shell**2)
    number_electrons -= 2*shell**2
    shell += 1
final_list.append(number_electrons)
print(final_list)
