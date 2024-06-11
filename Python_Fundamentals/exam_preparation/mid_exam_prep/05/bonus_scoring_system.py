number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
students_attendances = []
students_final_bonuses = []

for student in range(number_of_students):
    students_attendances.append(int(input()))
    try:
        students_final_bonuses.append(round(students_attendances[student] / number_of_lectures * (5 + additional_bonus)))
    except ZeroDivisionError:
        students_final_bonuses.append(0)

try:
    print(f'Max Bonus: {max(students_final_bonuses)}.')
    print(f'The student has attended {students_attendances[students_final_bonuses.index(max(students_final_bonuses))]} lectures.')
except ValueError:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
