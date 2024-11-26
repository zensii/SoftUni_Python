from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    BASE_PROTECTION = 120
    BASE_PRICE = 15.0

    def __init__(self):
        super().__init__(self.BASE_PROTECTION, self.BASE_PRICE)

    def increase_price(self):
        self.price *= 1.2