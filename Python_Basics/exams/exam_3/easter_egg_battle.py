p1_eggs = int(input())
p2_eggs = int(input())

while True:
    user_input = input()

    if user_input == "End":
        print(f'Player one has {p1_eggs} eggs left.')
        print(f'Player two has {p2_eggs} eggs left.')
        break
    else:
        if user_input == 'one':
            p2_eggs -= 1
        elif user_input == 'two':
            p1_eggs -= 1
    if p1_eggs == 0:
        print(f'Player one is out of eggs. Player two has {p2_eggs} eggs left.')
        break
    elif p2_eggs == 0:
        print(f'Player two is out of eggs. Player one has {p1_eggs} eggs left.')
        break
