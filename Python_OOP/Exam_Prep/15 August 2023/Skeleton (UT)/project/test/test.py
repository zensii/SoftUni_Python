from project.trip import Trip
from unittest import TestCase, main

class TestTrip(TestCase):

    def setUp(self):
        self.family_trip = Trip(100.5, 4, True)
        self.friends_trip = Trip(100.5, 4, False)

    def test_init(self):
        self.assertEqual(100.5, self.family_trip.budget)
        self.assertEqual(100.5, self.family_trip.budget)
        self.assertTrue(self.family_trip.is_family)
        self.assertFalse(self.friends_trip.is_family)
        self.assertEqual({}, self.family_trip.booked_destinations_paid_amounts)
        self.assertEqual({'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}, self.family_trip.DESTINATION_PRICES_PER_PERSON)

    def test_travellers_ok(self):
        self.family_trip.travelers = 10
        self.assertEqual(10, self.family_trip.travelers)

    def test_travellers_nok(self):
        with self.assertRaises(ValueError) as ve:
            self.family_trip.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_negative_travellers_nok(self):
        with self.assertRaises(ValueError) as ve:
            self.family_trip.travelers = -4
        self.assertEqual('At least one traveler is required!', str(ve.exception))


    def test_is_family_false(self):
        self.family_trip.is_family = False
        self.assertFalse(self.family_trip.is_family)

    def test_is_family_less_tann_two_ppl(self):
        self.family_trip.travelers = 1
        self.family_trip.is_family = True
        self.assertFalse(self.family_trip.is_family)

    def test_is_family_no_info(self):
        self.family_trip.is_family = None
        self.assertFalse(self.family_trip.is_family)

    def test_book_a_trip_dest_not_available(self):
        self.assertEqual('This destination is not in our offers, please choose a new one!', self.family_trip.book_a_trip('Sofia'))

    def test_book_a_trip_no_money_friends(self):
        self.friends_trip.budget = 0
        self.assertEqual('Your budget is not enough!', self.friends_trip.book_a_trip('Brazil'))

    def test_book_a_trip_no_money_family(self):
        self.family_trip.budget = 0
        self.assertEqual('Your budget is not enough!', self.family_trip.book_a_trip('Brazil'))


    def test_book_a_trip_family_ok_friends_nok(self):
        self.family_trip.budget = 1800
        self.friends_trip.budget = 1800
        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 0.00', self.family_trip.book_a_trip('Bulgaria'))
        self.assertEqual('Your budget is not enough!', self.friends_trip.book_a_trip('Bulgaria'))


    def test_book_a_trip_family_nok_friends_ok(self):
        self.family_trip.budget = 0
        self.friends_trip.budget = 18000
        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 16000.00', self.friends_trip.book_a_trip('Bulgaria'))
        self.assertEqual('Your budget is not enough!', self.family_trip.book_a_trip('Bulgaria'))


    def test_paid_amounts_is_updated(self):
        self.family_trip.budget = 1800
        self.family_trip.book_a_trip('Bulgaria')
        self.assertEqual({'Bulgaria': 1800}, self.family_trip.booked_destinations_paid_amounts)

    def test_booking_status_not_ready(self):
        self.assertEqual('No bookings yet. Budget: 100.50', self.family_trip.booking_status())

    def test_booking_status_ok(self):
        self.family_trip.budget = 1800
        self.family_trip.book_a_trip('Bulgaria')
        self.assertEqual('Booked Destination: Bulgaria\nPaid Amount: 1800.00\nNumber of Travelers: 4\nBudget Left: 0.00', self.family_trip.booking_status())


if __name__ == '__main__':
    main()
