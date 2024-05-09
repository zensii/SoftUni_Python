student = 0
standard = 0
kid = 0
total_watchers = 0
The_End = False

while not The_End:
    command = input()
    if command == "Finish":
        The_End = True
        continue
    movie_title = command
    watchers = 0
    total_seats = int(input())
    for _ in range(total_seats):
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'kid':
            kid += 1
        elif ticket_type == 'student':
            student += 1
        else:
            standard += 1
        watchers += 1
        total_watchers += 1
    print(f'{movie_title} - {watchers / total_seats * 100:.2f}% full.')
else:
    print(f'Total tickets: {total_watchers}')
    print(f'{student / total_watchers * 100:.2f}% student tickets.')
    print(f'{standard / total_watchers * 100:.2f}% standard tickets.')
    print(f'{kid / total_watchers * 100:.2f}% kids tickets.')
