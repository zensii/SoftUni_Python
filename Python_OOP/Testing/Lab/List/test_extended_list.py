from pkgutil import get_data
from unittest import TestCase, main

# from Python_OOP.Testing.Lab.List.extended_list import IntegerList


class TestList(TestCase):

    def setUp(self):
        self.int_list = IntegerList(1, "Not an Integer")

    def test_add_exception(self):
        with self.assertRaises(ValueError) as ex:
           self.int_list.add(5.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_ok(self):
        self.int_list.add(5)
        self.assertEqual([1, 5], self.int_list.get_data())

    def test_remove_index_exception(self):
        with self.assertRaises(IndexError) as ex:
           self.int_list.remove_index(len(self.int_list.get_data()) + 1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index(self):
        expected_result = self.int_list.get_data()[0]
        self.assertEqual(expected_result, self.int_list.remove_index(0))
        self.assertEqual([], self.int_list.get_data())

    def test_initialization(self):
       self.assertEqual([1], self.int_list.get_data())

    def test_get_exception(self):
        with self.assertRaises(IndexError) as ex:
           self.int_list.get(len(self.int_list.get_data()) + 1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_ok(self):
        self.assertEqual(1, self.int_list.get(0))

    def test_insert_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(len(self.int_list.get_data()), 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_not_integer_element(self):
        with self.assertRaises(ValueError) as ex:
            self.int_list.insert(0, 5.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_ok(self):
        expected_result = [2, 1]
        self.int_list.insert(-1, 2)
        self.assertEqual(expected_result, self.int_list.get_data())

    def test_get_biggest(self):
        self.int_list.get_data().append(5)
        expected_result = 5
        self.assertEqual(expected_result, self.int_list.get_biggest())

    def test_get_index(self):
        self.assertEqual(0, self.int_list.get_index(1))


if __name__ == '__main__':
    main()