coffee_need = ['coding', 'cat', 'dog', 'movie']
coffees = 0
coffee_need_upper = list()

for word in coffee_need:
    coffee_need_upper.append(word.upper())

while True:
    user_input = input()

    if user_input == 'END':
        pass

        break
    elif user_input in coffee_need:
        coffees += 1
    elif user_input in coffee_need_upper:
        coffees += 2
    else:
        continue
if coffees > 5:
    print('You need extra sleep')
else:
    print(coffees)
