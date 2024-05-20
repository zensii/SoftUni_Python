a = int(input())
b = int(input())
temp = 0

print(f'Before:\na = {a}\nb = {b}')

c = b
b = a
a = c

print(f'After:\na = {a}\nb = {b}')