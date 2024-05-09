jury = int(input())
grand_total = 0
counter = 0

while True:
    command = input()
    if command == 'Finish':
        print(f"Student's final assessment is {grand_total/counter:.2f}.")
        break
    else:
        presentation_name = command
        total_score = 0
        for _ in range(jury):
            score = float(input())
            total_score += score
            grand_total += score
            counter += 1
    print(f'{presentation_name} - {total_score/jury:.2f}.')
