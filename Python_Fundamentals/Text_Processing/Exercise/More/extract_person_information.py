n = int(input())
users = {}
for i in range(n):
    usr_input = input()
    name = usr_input.split('|')[0].split('@')[1]
    age = usr_input.split('*')[0].split('#')[1]
    users[name] = age

for name, age in users.items():
    print(f'{name} is {age} years old.')
