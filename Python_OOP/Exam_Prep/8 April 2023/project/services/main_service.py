from project.services.base_service import BaseService


class MainService(BaseService):
    BASE_CAPACITY = 30
    TYPE = 'MainService'
    def __init__(self, name: str):
        super().__init__(name, self.BASE_CAPACITY)

    def details(self):
        result = f"{self.name} Main Service:\nRobots: "
        robot_names = ' '.join(r.name for r in self.robots)
        if not robot_names:
            result += 'none'
        else:
            result += robot_names
        return result