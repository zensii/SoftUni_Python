from project_03.employee import Employee
from project_03.person import Person


class Teacher(Person,Employee):

    def teach(self):
        return 'teaching...'