from unittest import main, TestCase

from Python_OOP.Testing.Lab.TestCat.test_cat import Cat # need to comment out for Judge


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat('Kitty')

    def test_eat_no_exception(self):

        expected_result = self.cat.size + 1
        self.cat.eat()
        self.assertEqual(expected_result, self.cat.size)
        self.assertTrue(self.cat.fed)

    def test_eat_with_exception_because_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep_with_exception_because_hungry(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):

        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
