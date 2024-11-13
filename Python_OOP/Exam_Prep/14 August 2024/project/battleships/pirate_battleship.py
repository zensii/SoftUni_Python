from project.battleships.base_battleship import BaseBattleship


class PirateBattleship(BaseBattleship):
    AMMO = 80

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.AMMO)

        self.ship_type = 'PirateBattleship'

    def attack(self):
        self.ammunition -= 10