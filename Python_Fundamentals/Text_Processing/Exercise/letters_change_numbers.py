def calculate_first(letter, number):
    if letter.isupper():
        return number / (ord(letter)-64)
    else:
        return number * (ord(letter)-96)


def calculate_last(letter, number):
    if letter.isupper():
        return number - (ord(letter)-64)
    else:
        return number + (ord(letter)-96)


input_string = [string.strip() for string in input().split()]
total_sum = 0

for string in input_string:

    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])
    result = calculate_first(first_letter, number)
    total_sum += calculate_last(last_letter, result)

print(f'{total_sum:.2f}')
