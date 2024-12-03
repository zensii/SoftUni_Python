from unittest import TestCase, main
from project.toy_store import ToyStore

class TestToyStore(TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_init(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_add_toy_raises_shelf_not_present(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('XXX', 'TeddyBear')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_raises_toy_already_present(self):
        self.toy_store.toy_shelf["A"] = "TeddyBear"
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'TeddyBear')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_raises_shelf_occupied(self):
        self.toy_store.toy_shelf["A"] = "TeddyBear"
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', 'ToyCar')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_ok(self):
        result = self.toy_store.add_toy("A", "ToyCar")
        self.assertEqual("Toy:ToyCar placed successfully!", result)
        self.assertEqual('ToyCar', self.toy_store.toy_shelf['A'])

    def test_remove_toy_raises_shelf_not_present(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('XXX', 'TeddyBear')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_raises_toy_not_present(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', 'TeddyBear')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_ok(self):
        self.toy_store.toy_shelf['A'] = 'TeddyBear'
        result = self.toy_store.remove_toy('A', 'TeddyBear')
        self.assertEqual("Remove toy:TeddyBear successfully!", result)
        self.assertEqual(None, self.toy_store.toy_shelf['A'])

if __name__ == '__main__':
    main()