students_database = []

command = input()

while command[0].isupper():
    student_data = command.split(':')

    # name = student_data[0]
    # ID = student_data[1]
    # course = student_data[2]

    name, ID, course = student_data

    students_database.append({"name": name, "ID": ID, "course": course})

    command = input()

course_to_search = command

for student in students_database:
    if student['course'][0:3] == course_to_search[0:3]:
        print(f"{student['name']} - {student['ID']}")
