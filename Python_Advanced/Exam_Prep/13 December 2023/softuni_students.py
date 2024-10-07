def softuni_students(*args, **kwargs):
    student_dict = {}

    for arg in args:
        course_id, student_id = arg
        student_dict.setdefault(student_id, []).append(course_id)

    for course_id, course_name in kwargs.items():
        for student_it, courses in student_dict.items():
            if course_id in courses:
                courses[courses.index(course_id)] = course_name

    sorted_students_dict = dict(sorted(student_dict.items()))
    result = ''
    failed_students = []

    for student, course in sorted_students_dict.items():
        if 'id' not in course[0]:
            result += f"*** A student with the username {student} has successfully finished the course {course[0]}!\n"
        else:
            failed_students.append(student)
    if failed_students:
        result += f"!!! Invalid course students: {', '.join(failed_students)}"

    return result


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
