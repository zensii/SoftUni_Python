from project_01.food import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date):
        self.name = name
        super().__init__(expiration_date)
