from statistics import mean


def add_grades(n, database):
    for entry in range(n):
        student_name = input()
        grade = float(input())

        if student_name not in database:
            database[student_name] = [grade]
        else:
            database[student_name].append(grade)

    return database


def calculate_average_score(database):
    filtered_database = {}
    for student in database:
        average_score = mean(database[student])
        if average_score >= 4.50:
            filtered_database[student] = average_score
    return filtered_database


def main():
    my_dict = {}
    student_inputs = int(input())
    my_dict = add_grades(student_inputs, my_dict)
    my_dict = calculate_average_score(my_dict)

    for student, average_score in my_dict.items():
        print(f'{student} -> {average_score:.2f}')


if __name__ == '__main__':
    main()
