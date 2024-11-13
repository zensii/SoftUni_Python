from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, model: str, price: float, material: str, sub_type: str):
        self.model = model
        self.price = price
        self.material = material
        self.sub_type = sub_type

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model_str: str):
        if len(model_str) < 3 or model_str.isspace():
            raise ValueError("Product model must be at least 3 chars long!")
        self._model = model_str

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price_value):
        if price_value <= 0.0:
            raise ValueError("Product price must be greater than zero!")
        self._price = price_value

    @abstractmethod
    def discount(self):
        pass