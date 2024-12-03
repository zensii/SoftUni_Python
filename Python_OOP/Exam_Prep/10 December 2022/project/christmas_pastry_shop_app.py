from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    ALLOWED_DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    ALLOWED_BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.ALLOWED_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        current_menu = [d.name for d in self.delicacies if d.name == name]
        if name in current_menu:
            raise Exception(f"{name} already exists!")
        new_delicacy = self.ALLOWED_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth_present = [b for b in self.booths if b.booth_number == booth_number]
        if booth_present:
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in self.ALLOWED_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")
        new_booth = self.ALLOWED_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        not_reserved_booths = [b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people]
        if not not_reserved_booths:
            raise Exception(f"No available booth for {number_of_people} people!")
        selected_booth = not_reserved_booths[0]
        selected_booth.reserve(number_of_people)
        return f"Booth {selected_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = [b for b in self.booths if b.booth_number == booth_number]
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")
        delicacy_available = [d for d in self.delicacies if d.name == delicacy_name]
        if not delicacy_available:
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth[0].delicacy_orders.append(delicacy_available[0])
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        bill = booth.price_for_reservation + sum([o.price for o in booth.delicacy_orders])
        self.income += bill
        booth.is_reserved = False
        booth.price_for_reservation = 0
        booth.delicacy_orders = []
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."