students_number = int(input())
students = {}
for i in range(students_number):
    name, grade = input().split()
    grade = float(grade.format())
    students[name] = students.get(name, [])
    students[name].append(grade)

for student, grades in students.items():
    print(f"{student} -> {' '.join([str(format(grade, '.2f')) for grade in grades])} (avg: {sum(grades)/len(grades):.2f})")
