from project.senior_student import SeniorStudent

from unittest import TestCase, main

class TestSeniorStudent(TestCase):
    def setUp(self):
        self.student = SeniorStudent('12345', 'Ivan', 10.0)

    def test_init(self):
        self.assertEqual('12345', self.student.student_id)
        self.assertEqual('Ivan', self.student.name)
        self.assertEqual(10.0, self.student.student_gpa)
        self.assertEqual(set(), self.student.colleges)

    def test_id_raises_less_than_4(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_id = '123'
        self.assertEqual("Student ID must be at least 4 digits long!", str(ve.exception))

    def test_name_raises_null(self):
        with self.assertRaises(ValueError) as ve:
            self.student.name = ' '
        self.assertEqual("Student name cannot be null or empty!", str(ve.exception))

    def test_gpa_raises_less_than_1(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_gpa = 0.5
        self.assertEqual("Student GPA must be more than 1.0!", str(ve.exception))

    def test_gpa_raises_equal_1(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_gpa = 1.0
        self.assertEqual("Student GPA must be more than 1.0!", str(ve.exception))

    def test_apply_to_college_failed_lower_gpa(self):
        gpa_required = 11
        self.assertEqual('Application failed!', self.student.apply_to_college(gpa_required,'tu'))

    def test_apply_to_college_ok(self):
        gpa_required = 9
        self.assertEqual('Ivan successfully applied to tu.', self.student.apply_to_college(gpa_required,'tu'))
        self.assertEqual({'TU'}, self.student.colleges)
        self.assertEqual(1, len(self.student.colleges))

    def test_college_apply_twice(self):
        self.student.colleges.add('TU')
        gpa_required = 9
        self.assertEqual('Ivan successfully applied to tu.', self.student.apply_to_college(gpa_required,'tu'))
        self.assertEqual({'TU'}, self.student.colleges)
        self.assertEqual(1, len(self.student.colleges))

    def test_update_gpa_not_updated(self):
        new_gpa = 1.0
        self.assertEqual('The GPA has not been changed!', self.student.update_gpa(new_gpa))
        self.assertEqual(10.0, self.student.student_gpa)

    def test_update_gpa_ok(self):
        new_gpa = 15.0
        self.assertEqual('Student GPA was successfully updated.', self.student.update_gpa(new_gpa))
        self.assertEqual(15.0, self.student.student_gpa)

    def test___eq__true(self):
        other_student = SeniorStudent('9999', 'Iceman', 10.0)
        self.assertTrue(self.student == other_student)

    def test___eq__false(self):
        other_student = SeniorStudent('9999', 'Iceman', 999.0)
        self.assertFalse(self.student == other_student)

if __name__ == '__main__':
    main()