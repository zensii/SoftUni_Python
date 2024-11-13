from typing import List

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):

        valid_products = ["Chair", "HobbyHorse"]

        if product_type not in valid_products:
            raise Exception("Invalid product type!")
        product = Chair(model, price) if product_type == 'Chair' else HobbyHorse(model, price)
        self.products.append(product)

        return f"A product of sub-type {product.sub_type} was produced."


    def register_new_store(self, store_type: str, name: str, location: str):

        valid_stores = ['FurnitureStore', 'ToyStore']

        if store_type not in valid_stores:
            raise Exception(f"{store_type} is an invalid type of store!")
        store = FurnitureStore(name, location) if store_type == 'FurnitureStore' else ToyStore(name, location)
        self.stores.append(store)

        return f"A new {store_type} was successfully registered."


    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        qty_sold = 0

        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."
        for product in products:
            if store.store_type.lower().startswith(product.sub_type.lower()):
                store.products.append(product)
                store.capacity -= 1
                self.products.remove(product)
                self.income += product.price
                qty_sold += 1
        if qty_sold > 0:
            return f"Store {store.name} successfully purchased {qty_sold} items."
        return "Products do not match in type. Nothing sold."


    def unregister_store(self, store_name: str):

        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            raise Exception(f"No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."


    def discount_products(self, product_model: str):

        products_to_discount = [p for p in self.products if p.model == product_model]
        if len(products_to_discount) > 0:

            for pr in products_to_discount:
                pr.discount()

        return f"Discount applied to {len(products_to_discount)} products with model: {product_model}"


    def request_store_stats(self, store_name: str):

        store = next((s for s in self.stores if s.name == store_name), None)
        if store is None:
            return f"There is no store registered under this name!"
        return store.store_stats()


    def statistics(self):
        models = set(p.model for p in self.products)
        stores = [st.name for st in self.stores]

        result = (f"Factory: {self.name}\n"
                  f"Income: {self.income:.2f}\n"
                  "***Products Statistics***\n"
                  f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}")

        for model in sorted(list(models)):
            count_model = len([p for p in self.products if p.model == model])
            result += f"\n{model}: {count_model}"


        result += f"\n***Partner Stores: {len(self.stores)}***"

        for store in sorted(stores):
            result += f"\n{store}"

        return result


# Initialize the FactoryManager
factory_manager = FactoryManager("Cool Factory")

# Produce some items
print(factory_manager.produce_item("Chair", "Classic", 80.0))
print(factory_manager.produce_item("Chair", "Modern", 100.0))
print(factory_manager.produce_item("Chair", "Modern", 200.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 120.0))
print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 100.0))
print()

# Register new stores
print(factory_manager.register_new_store("FurnitureStore", "Furniture Outlet", "SOF"))
print(factory_manager.register_new_store("ToyStore", "Toy World", "VAR"))
print()

# Sell products to stores
chair1 = factory_manager.products[0]
chair2 = factory_manager.products[1]
chair3 = factory_manager.products[2]
store1 = factory_manager.stores[0]
store2 = factory_manager.stores[1]
print(factory_manager.sell_products_to_store(store2, chair1, chair2))
print(factory_manager.sell_products_to_store(store1, chair1, chair2, chair3))
print()

# Unregister store
print(factory_manager.unregister_store("Furniture Outlet"))
print()

# Discount products
print(factory_manager.discount_products("Classic"))
print(factory_manager.discount_products("Rocking Horse"))
print()

# Request store statistics
print(factory_manager.request_store_stats("Furniture Outlet"))
print(factory_manager.request_store_stats("Toy World"))
print()

# Factory statistics
print(factory_manager.statistics())
print()

# Unregister store
print(factory_manager.unregister_store("Toy World"))

