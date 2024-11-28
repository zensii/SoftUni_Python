from project.second_hand_car import SecondHandCar
from unittest import TestCase, main

class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar('Mercedes', 'sedan', 800_000, 1500)

    def test_init(self):
        self.assertEqual('Mercedes', self.car.model)
        self.assertEqual('sedan', self.car.car_type)
        self.assertEqual(800_000, self.car.mileage)
        self.assertEqual(1500, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.0
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_mileage_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_set_promotional_price_ok(self):
        result = self.car.set_promotional_price(1000)
        self.assertEqual(1000, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_set_promotional_price_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2000)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_need_repair_ok(self):
        result = self.car.need_repair(500, 'painting')
        self.assertEqual(2000, self.car.price)
        self.assertEqual('Price has been increased due to repair charges.', result)
        self.assertEqual(['painting'], self.car.repairs)

    def test_need_repair_raises(self):
        result = self.car.need_repair(2000, 'new engine')
        self.assertEqual('Repair is impossible!', result)
        self.assertEqual([], self.car.repairs)

    def test_gt_ok(self):
        car2 = SecondHandCar('Toyota', 'sedan', 600_000, 2000)
        self.assertTrue(car2 > self.car)
        self.assertFalse(self.car > car2)

    def test_gt_not_same_types(self):
        car2 = SecondHandCar('Toyota', 'coupe', 600_000, 2000)
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.car > car2)

    def test_str(self):
        result = str(self.car)
        expected = "Model Mercedes | Type sedan | Milage 800000km\nCurrent price: 1500.00 | Number of Repairs: 0"
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()