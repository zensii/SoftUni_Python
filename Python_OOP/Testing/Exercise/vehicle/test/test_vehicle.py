from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.car = Vehicle(100, 100)


    def test_init(self):
        self.assertEqual(100.0, self.car.fuel)
        self.assertEqual(100.0, self.car.horse_power)
        self.assertEqual(100.0, self.car.capacity)
        self.assertEqual(1.25, self.car.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_ok(self):
        self.car.drive(4)
        self.assertEqual(95, self.car.fuel)

    def test_drive_exception(self):
        self.car.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_ok(self):
        self.car.fuel = 50
        self.car.refuel(10)
        self.assertEqual(60, self.car.fuel)

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test___str__(self):
        self.assertEqual("The vehicle has 100 horse power with 100 fuel left and 1.25 fuel consumption", self.car.__str__())

if __name__ == '__main__':
    main()