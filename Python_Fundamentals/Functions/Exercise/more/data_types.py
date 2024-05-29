def data_type(type_data, number):
    if type_data == 'int':
        return int(number) * 2
    elif type_data == 'real':
        return f'{float(number) * 1.5:.2f}'
    elif type_data == 'string':
        return '$' + number + '$'


type_data = input()
number = input()
print(data_type(type_data, number))
