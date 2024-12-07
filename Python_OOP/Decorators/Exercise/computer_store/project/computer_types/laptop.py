from project.computer_types.computer import Computer
import math

class Laptop(Computer):
    TYPE_NAME = 'Laptop'
    AVAILABLE_PROCESSORS = {'AMD Ryzen 9 5950X': 900, 'Intel Core i9-11900H': 1050, 'Apple M1 Pro': 1200}
    MAX_RAM = 64

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{ processor } is not compatible with laptop {self.manufacturer} {self.model}!")
        power = math.log2(ram)
        if ram > self.MAX_RAM or power > int(power):
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        ram_price = power * 100
        self.ram = ram
        self.processor = processor
        self.price = ram_price + self.AVAILABLE_PROCESSORS[processor]

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price:.0f}$."
