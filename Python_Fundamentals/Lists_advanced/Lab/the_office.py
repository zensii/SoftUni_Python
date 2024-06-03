happiness_levels = list(map(int, input().split()))
mult_factor = int(input())

modified_happiness = list(map(lambda x: x * mult_factor, happiness_levels))

average_happiness = sum(modified_happiness) / len(modified_happiness)

happy_employees = list(filter(lambda x: x > average_happiness, modified_happiness))

if len(happy_employees) >= len(happiness_levels) / 2:
    print(f'Score: {len(happy_employees)}/{len(happiness_levels)}. Employees are happy!')
else:
    print(f'Score: {len(happy_employees)}/{len(happiness_levels)}. Employees are not happy!')
