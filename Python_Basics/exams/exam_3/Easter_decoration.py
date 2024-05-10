clients = int(input())
earnings = 0

for client in range(clients):

    baskets = 0
    wreaths = 0
    bunnies = 0
    bill = 0
    discount = 0

    while True:
        user_input = input()

        if user_input == 'Finish':
            if (baskets + wreaths + bunnies) % 2 == 0:
                discount = 0.2
            bill = (baskets * 1.5 + wreaths * 3.8 + bunnies * 7) * (1 - discount)
            earnings += bill
            print(f'You purchased {baskets+wreaths+bunnies} items for {bill:.2f} leva.')

            break
        elif user_input == 'basket':
            baskets += 1
        elif user_input == 'wreath':
            wreaths += 1
        elif user_input == 'chocolate bunny':
            bunnies += 1

print(f'Average bill per client is: {earnings / clients:.2f} leva.')
