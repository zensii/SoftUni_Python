from project.robot import Robot

import unittest


class TestRobot(unittest.TestCase):

    # Robot initialization with valid parameters creates instance with correct attributes
    def test_valid_robot_initialization(self):
        robot = Robot("R2D2", "Military", 100, 1000.0)

        self.assertEqual(robot.robot_id, "R2D2")
        self.assertEqual(robot.category, "Military")
        self.assertEqual(robot.available_capacity, 100)
        self.assertEqual(robot.price, 1000.0)
        self.assertEqual(robot.hardware_upgrades, [])
        self.assertEqual(robot.software_updates, [])

    # Initializing robot with invalid category raises ValueError
    def test_invalid_category_initialization(self):
        with self.assertRaises(ValueError) as context:
            Robot("R2D2", "Invalid", 100, 1000.0)

        self.assertEqual(
            str(context.exception),
            "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'"
        )

    # Upgrading hardware with new component increases price and adds to hardware_upgrades list
    def test_upgrade_hardware_increases_price_and_adds_component(self):
        robot = Robot(robot_id="R1", category="Military", capacity=100, price=1000.0)
        initial_price = robot.price
        component_price = 200.0
        result = robot.upgrade("Laser", component_price)
        self.assertIn("Laser", robot.hardware_upgrades)
        self.assertEqual(robot.price, initial_price + component_price * Robot.PRICE_INCREMENT)
        self.assertEqual(result, "Robot R1 was upgraded with Laser.")

    # Software update with higher version and sufficient capacity updates version and reduces capacity
    def test_software_update_with_sufficient_capacity(self):
        robot = Robot(robot_id="R2", category="Education", capacity=50, price=500.0)
        initial_capacity = robot.available_capacity
        version = 2.0
        needed_capacity = 20
        result = robot.update(version, needed_capacity)
        self.assertIn(version, robot.software_updates)
        self.assertEqual(robot.available_capacity, initial_capacity - needed_capacity)
        self.assertEqual(result, "Robot R2 was updated to version 2.0.")

    # Price comparison between robots returns correct comparison message
    def test_price_comparison_between_robots(self):
        robot1 = Robot(robot_id="R3", category="Entertainment", capacity=30, price=1500.0)
        robot2 = Robot(robot_id="R4", category="Humanoids", capacity=40, price=1500.0)
        result_equal = robot1 > robot2
        self.assertEqual(result_equal, "Robot with ID R3 costs equal to Robot with ID R4.")

        robot2.price = 1600.0
        result_cheaper = robot1 > robot2
        self.assertEqual(result_cheaper, "Robot with ID R3 is cheaper than Robot with ID R4.")

        robot1.price = 1700.0
        result_more_expensive = robot1 > robot2
        self.assertEqual(result_more_expensive, "Robot with ID R3 is more expensive than Robot with ID R4.")

    # Setting valid category from ALLOWED_CATEGORIES works correctly
    def test_setting_valid_category(self):
        robot = Robot(robot_id="R1", category="Military", capacity=10, price=1000.0)
        self.assertEqual(robot.category, "Military")
        robot.category = "Education"
        self.assertEqual(robot.category, "Education")

    # Setting negative price raises ValueError
    def test_setting_negative_price_raises_value_error(self):
        robot = Robot(robot_id="R2", category="Entertainment", capacity=5, price=500.0)
        with self.assertRaises(ValueError) as context:
            robot.price = -100.0
        self.assertEqual(str(context.exception), "Price cannot be negative!")

    # Setting positive price value works correctly
    def test_setting_positive_price(self):
        robot = Robot(robot_id="R1", category="Education", capacity=10, price=100.0)
        robot.price = 150.0
        self.assertEqual(robot.price, 150.0)

    # Attempting duplicate hardware upgrade returns not upgraded message
    def test_duplicate_hardware_upgrade(self):
        robot = Robot(robot_id="R2", category="Military", capacity=20, price=200.0)
        robot.upgrade("Laser", 50.0)
        result = robot.upgrade("Laser", 50.0)
        self.assertEqual(result, "Robot R2 was not upgraded.")

    # Software update with lower/equal version returns not updated message
    def test_software_update_lower_equal_version(self):
        robot = Robot(robot_id="R3", category="Entertainment", capacity=30, price=300.0)
        robot.update(1.0, 5)
        result = robot.update(1.0, 5)
        self.assertEqual(result, "Robot R3 was not updated.")