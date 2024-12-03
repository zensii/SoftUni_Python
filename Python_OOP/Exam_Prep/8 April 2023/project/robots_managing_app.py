from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    ALLOWED_SERVICES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ALLOWED_ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.ALLOWED_SERVICES:
            raise Exception("Invalid service type!")
        new_service = self.ALLOWED_SERVICES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ALLOWED_ROBOT_TYPES:
            raise Exception("Invalid robot type!")
        new_robot = self.ALLOWED_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        service = self.get_service(service_name)
        robot = [r for r in self.robots if r.name == robot_name][0]

        if robot.POSSIBLE_SERVICE != service.__class__.__name__:
            return "Unsuitable service."
        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.get_service(service_name)
        robot = next((r for r in service.robots if r.name == robot_name), None)
        if robot is None:
            raise Exception(f"No such robot in this service!")
        self.robots.append(robot)
        service.robots.remove(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.get_service(service_name)
        fed = 0
        for robot in service.robots:
            robot.eating()
            fed += 1
        return f"Robots fed: {fed}."

    def service_price(self, service_name: str):
        service = self.get_service(service_name)
        total_price = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())
        return '\n'.join(result)

    def get_service(self, service_name):
        service = next((s for s in self.services if s.name == service_name), None)
        if service is None:
            raise Exception('Service not found')
        return service