from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    CAPACITY = 50
    STORE_TYPE = 'FurnitureStore'

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.CAPACITY)

    @property
    def store_type(self):
        return self.STORE_TYPE

    def store_stats(self):

        all_models = list(map(lambda m: m.model, self.products))

        result = f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
        result += f"{self.get_estimated_profit()}\n"
        result += "**Furniture for sale:"

        for model in sorted(list(set(all_models))):
            count_products = all_models.count(model)
            combined_model_price = sum(p.price for p in self.products if p.model == model)
            result += f"\n{model}: {count_products}pcs, average price: {(combined_model_price / count_products):.2f}"

        return result