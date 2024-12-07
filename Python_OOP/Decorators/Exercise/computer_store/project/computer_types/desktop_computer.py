from project.computer_types.computer import Computer
import math

class DesktopComputer(Computer):
    TYPE_NAME = 'Desktop Computer'
    AVAILABLE_PROCESSORS = {'AMD Ryzen 7 5700G': 500, 'Intel Core i5-12600K': 600, 'Apple M1 Max': 1800}
    MAX_RAM = 128

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{ processor } is not compatible with desktop computer {self.manufacturer} {self.model}!")
        power = math.log2(ram)
        if ram > self.MAX_RAM or power > int(power):
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        ram_price = power * 100
        self.ram = ram
        self.processor = processor
        self.price = ram_price + self.AVAILABLE_PROCESSORS[processor]
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price:.0f}$."

