from abc import ABC, abstractmethod
from typing import List

from project.products.base_product import BaseProduct


class BaseStore(ABC):
    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: List[BaseProduct] = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_str):
        if name_str.isspace() or name_str == '':
            raise ValueError("Store name cannot be empty!")
        self._name = name_str

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location_str: str):
        if not len(location_str) == 3 or any(char.isspace() for char in location_str):
            raise ValueError("Store location must be 3 chars long!")
        self._location = location_str

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, cap_value):
        if cap_value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self._capacity = cap_value

    def get_estimated_profit(self):
        profit = 0.1
        prod_value = sum(p.price for p in self.products)
        future_profit = prod_value * profit
        return f"Estimated future profit for {len(self.products)} products is {future_profit:.2f}"

    @property
    @abstractmethod
    def store_type(self):
        pass

    @abstractmethod
    def store_stats(self):
        pass