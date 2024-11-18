from unittest import TestCase,main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal('Bobo', 'Gorilla', 'U..U..U..')

    def test_init(self):
        self.assertEqual('Bobo', self.mammal.name)
        self.assertEqual('Gorilla', self.mammal.type)
        self.assertEqual('U..U..U..', self.mammal.sound)
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_make_sound_ok(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == '__main__':
    main()