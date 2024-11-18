from unittest import TestCase, main

from Python_OOP.Testing.Lab.CarManager.car_manager import Car


class TestCarManager(TestCase):
    def setUp(self):
        self.test_car = Car('Citroen', 'C4', 7, 50)

    def test_correct_init(self):
        self.assertEqual('Citroen', self.test_car.make)
        self.assertEqual('C4', self.test_car.model)
        self.assertEqual(7, self.test_car.fuel_consumption)
        self.assertEqual(50, self.test_car.fuel_capacity)
        self.assertEqual(0, self.test_car.fuel_amount)

    def test_null_make(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_null_model(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_null_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_consumption = -5
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))


    def test_null_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_capacity = -5
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_ok(self):
        self.test_car.refuel(10)
        self.assertEqual(10, self.test_car.fuel_amount)


    def test_refuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))


    def test_drive_ok(self):
        self.test_car.fuel_amount = 10
        self.test_car.drive(100)
        self.assertEqual(3, self.test_car.fuel_amount)

    def test_drive_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
