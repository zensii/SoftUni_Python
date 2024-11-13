from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):

    AMMO = 100

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.AMMO)

        self.ship_type = 'RoyalBattleship'

    def attack(self):
        self.ammunition -= 25