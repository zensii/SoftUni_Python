input_list = list(map(int, input().split(', ')))

print(f'Positive:', ', '.join(str(numbers) for numbers in input_list if numbers >= 0))
print(f'Negative:', ', '.join(str(numbers) for numbers in input_list if numbers < 0))
print(f'Even:', ', '.join(str(numbers) for numbers in input_list if numbers % 2 == 0))
print('Odd:', ', '.join(str(numbers) for numbers in input_list if numbers % 2 != 0))
