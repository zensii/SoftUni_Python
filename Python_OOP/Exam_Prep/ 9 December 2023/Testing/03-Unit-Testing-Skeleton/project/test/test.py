from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation

class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation('Sofia')

    def test_init_ok(self):
        self.assertEqual('Sofia', self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_init_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = 'aa'
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board('some train info')
        self.assertEqual(deque(['some train info']), self.station.arrival_trains)

    def test_train_has_arrived_other_trains_first(self):
        self.station.arrival_trains.append('Train for Sofia')
        self.station.arrival_trains.appendleft('Train for Burgas')
        self.assertEqual(f"There are other trains to arrive before Train for Sofia.", self.station.train_has_arrived("Train for Sofia"))

    def test_train_has_arrived_ready_to_leave(self):
        self.station.arrival_trains.append('Train for Sofia')
        self.assertEqual(f"Train for Sofia is on the platform and will leave in 5 minutes.", self.station.train_has_arrived("Train for Sofia"))

    def test_train_has_arrived_no_trains(self):
        with self.assertRaises(IndexError) as ie:
            self.station.train_has_arrived("Train for Sofia")
        self.assertEqual(f"pop from an empty deque", str(ie.exception))

    def test_train_has_left_no_trains(self):
        self.assertFalse(self.station.train_has_left('Train for Sofia'))

    def test_train_has_left_train_but_others_first(self):
        self.station.departure_trains.append('Train for Sofia')
        self.assertFalse(self.station.train_has_left('Train for Anywhere'))

    def test_train_has_left_ok(self):
        self.station.departure_trains.append('Train for Sofia')
        self.assertTrue(self.station.train_has_left('Train for Sofia'))

if __name__ == '__main__':
    main()