def register_student(course, student, database):

    if course not in database:
        database[course] = [student]
    else:
        database[course].append(student)
    return database


def print_students(curriculum_db):
    for course in curriculum_db:
        print(f'{course}: {len(curriculum_db[course])}')
        for student in curriculum_db[course]:
            print(f'-- {student}')


def main():
    curriculum = {}
    while True:
        command = input()
        if command == 'end':
            break

        course, student = command.split(' : ')
        curriculum = register_student(course, student, curriculum)

    print_students(curriculum)


if __name__ == '__main__':
    main()



