from project.clients.base_client import BaseClient


class VIPClient(BaseClient):

    MEMBERSHIP = 'VIP'
    POINT_LIMIT = 5

    def __init__(self, name: str):
        super().__init__(name, self.MEMBERSHIP)

    def earning_points(self, order_amount: float):
        earned_points = int(order_amount // self.POINT_LIMIT)
        self.points += earned_points
        return earned_points