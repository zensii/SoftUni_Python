input_list = [int(num) for num in input().split()]

even_list = filter(lambda x: x % 2 == 0, input_list)

print(list(even_list))
