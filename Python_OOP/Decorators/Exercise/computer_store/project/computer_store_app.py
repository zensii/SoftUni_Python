from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_TYPES = {'Desktop Computer': DesktopComputer, 'Laptop': Laptop}
    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        new_computer = self.VALID_TYPES[type_computer](manufacturer, model)
        self.warehouse.append(new_computer)

        return  new_computer.configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer_available = [c for c in self.warehouse if c.price <= client_budget and c.processor == wanted_processor and c.ram >= wanted_ram]
        if not computer_available:
            raise Exception("Sorry, we don't have a computer for you.")
        pc_to_sell = computer_available[0]
        self.warehouse.remove(pc_to_sell)
        self.profits += client_budget - pc_to_sell.price
        return f"{pc_to_sell.__repr__()} sold for {client_budget}$."

