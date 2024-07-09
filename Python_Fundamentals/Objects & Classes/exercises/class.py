def average(iterable):
    return round(sum(iterable)/len(iterable), 2)


class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return average(self.grades)

    def __repr__(self):
        single_line = ""
        single_line += f"The students in {self.name}: "
        single_line += ', '.join(self.students)
        single_line += f". Average grade: {self.get_average_grade()}"
        return single_line


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
