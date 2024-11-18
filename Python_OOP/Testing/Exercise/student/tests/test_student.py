from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student('Ivancho')
        self.student2 = Student('Penka', {"Python": ['note1', 'note2']})

    def test_init(self):
        self.assertEqual('Ivancho', self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init_with_courses(self):
        self.assertEqual({"Python": ['note1', 'note2']}, self.student2.courses)

    def test_enroll_note_already_added(self):
        self.student.courses['Math'] = []
        self.assertEqual("Course already added. Notes have been updated.", self.student.enroll('Math', ['added notes']))
        self.assertEqual(['added notes'], self.student.courses['Math'])

    def test_enroll_note_already_added_add_notes_no(self):
        self.student.courses['Math'] = []
        self.assertEqual("Course already added. Notes have been updated.", self.student.enroll('Math', ['added notes'], add_course_notes='NO'))
        self.assertEqual(['added notes'], self.student.courses['Math'])

    def test_enroll_new_course_and_new_note_added(self):
        self.assertEqual("Course and course notes have been added.", self.student.enroll('Math', ['added notes']))
        self.assertEqual(['added notes'], self.student.courses['Math'])

    def test_enroll_new_course_and_new_note_added_added_notes_no(self):
        self.assertEqual("Course has been added.", self.student.enroll('Math', ['added notes'], add_course_notes='NO'))
        self.assertEqual([], self.student.courses['Math'])

    def test_enroll_just_add_new_course(self):
        self.assertEqual("Course has been added.", self.student.enroll('Math', [], 'NO'))
        self.assertEqual([], self.student.courses['Math'])

    def test_enroll_just_add_new_course_added_notes_YES(self):
        self.assertEqual("Course and course notes have been added.", self.student.enroll('Math', [], 'Y'))
        self.assertEqual([], self.student.courses['Math'])


    def test_add_note_ok(self):
        self.student.courses['Math'] = []
        self.assertEqual("Notes have been updated", self.student.add_notes('Math', 'added notes'))
        self.assertEqual(['added notes'], self.student.courses['Math'])

    def test_add_note_exception(self):
        with self.assertRaises(Exception) as ex:
             self.student.add_notes('Math', 'added notes')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_ok(self):
        self.student.courses['Math'] = []
        self.student.leave_course('Math')
        self.assertEqual({}, self.student.courses)

    def test_leave_course_exception(self):
        with self.assertRaises(Exception) as ex:
             self.student.leave_course('Math')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()