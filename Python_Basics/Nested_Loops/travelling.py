command = input()


while command != 'End':

    destination = command
    budget_needed = float(input())
    total_saved = 0

    while budget_needed > total_saved:
        saved = float(input())
        total_saved += saved

    print(f'Going to {destination}!')

    command = input()
