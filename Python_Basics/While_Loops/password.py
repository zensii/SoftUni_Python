user = input()
master_password = input()
password = input()

while password != master_password:
    password = input()

print(f'Welcome {user}!')
