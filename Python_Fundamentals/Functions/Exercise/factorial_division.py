def factorial_division(a, b):
    fact_a = 1
    fact_b = 1
    for num in range(a, 0, -1):
        fact_a *= num
    for num in range(b, 0, -1):
        fact_b *= num

    return fact_a / fact_b


first_number = int(input())
second_number = int(input())

print(f'{factorial_division(first_number, second_number):.2f}')
