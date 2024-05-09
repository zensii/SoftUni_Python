name = input()
grade = 1
total_score = 0
expel = 0

while grade <= 12:

    score = float(input())

    if score >= 4:

        grade += 1
        total_score += score

    else:
        expel += 1

    if expel >= 2:

        print(f'{name} has been excluded at {grade} grade')
        break

if expel != 2:

    print(f'{name} graduated. Average grade: {total_score / 12:.2f}')
