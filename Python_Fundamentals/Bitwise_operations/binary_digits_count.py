n = int(input())
binary = int(input())
counter = 0
binary_n = bin(n)[2:]

for digit in binary_n:
    if digit == str(binary):
        counter += 1

digits = 'zeroes' if binary == 0 else 'ones'

print(f'We have {counter} {digits}.')

