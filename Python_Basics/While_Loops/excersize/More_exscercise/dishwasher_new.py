bottles_detergent = int(input())
counter = 0
plates = 0
pots = 0

total_detergent = bottles_detergent * 750

while True:
    entry = input()
    if entry != 'End':
        counter += 1
        dishes = int(entry)
        if counter != 3:
            total_detergent -= dishes * 5
            plates += dishes
        else:
            total_detergent -= dishes * 15
            counter = 0
            pots += dishes
    else:
        if total_detergent >= 0:
            print('Detergent was enough!')
            print(f'{plates} dishes and {pots} pots were washed.')
            print(f'Leftover detergent {total_detergent} ml.')
            break

    if total_detergent < 0:
        print(f'Not enough detergent, {abs(total_detergent)} ml. more necessary!')
        break
