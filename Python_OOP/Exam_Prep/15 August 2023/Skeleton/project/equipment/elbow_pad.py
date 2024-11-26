from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    BASE_PROTECTION = 90
    BASE_PRICE = 25.0

    def __init__(self):
        super().__init__(self.BASE_PROTECTION, self.BASE_PRICE)

    def increase_price(self):
        self.price *= 1.1