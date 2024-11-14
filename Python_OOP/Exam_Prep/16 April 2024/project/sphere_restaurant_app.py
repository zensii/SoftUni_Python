from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):

        w_type = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}.get(waiter_type, None)
        if w_type is None:
            return f"{waiter_type} is not a recognized waiter type."
        waiter = w_type(waiter_name, hours_worked)

        if waiter_name in [w.name for w in self.waiters]:
            return f"{waiter_name} is already on the staff."
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):

        c_type = {"RegularClient": RegularClient, "VIPClient": VIPClient}.get(client_type, None)
        if c_type is None:
            return f"{client_type} is not a recognized client type."
        if client_name in [c.name for c in self.clients]:
            return f"{client_name} is already a client."
        self.clients.append(c_type(client_name))
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):

        waiter = next((w for w in self.waiters if w.name == waiter_name), None)
        if not waiter:
            return f"No waiter found with the name {waiter_name}."
        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):

        client = next((c for c in self.clients if c.name == client_name), None)
        if not client:
            return f"{client_name} is not a registered client."
        points_earned = client.earning_points(order_amount)
        return f"{client_name} earned {points_earned} points from the order."

    def apply_discount_to_client(self, client_name: str):

        client = next((c for c in self.clients if c.name == client_name), None)
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"
        discount, points = client.apply_discount()
        return f"{client_name} received a {discount}% discount. Remaining points {points}"

    def generate_report(self):
        result = ("$$ Monthly Report $$\n"
                  f"Total Earnings: ${sum(w.calculate_earnings() for w in self.waiters):.2f}\n"
                  f"Total Clients Unused Points: {sum(c.points for c in self.clients)}\n"
                  f"Total Clients Count: {len(self.clients)}\n"
                  f"** Waiter Details **")
        for waiter in sorted(self.waiters, key=lambda w: -w.calculate_earnings()):
            result += f"\n{str(waiter)}"

        return result

# Create an instance of SphereRestaurantApp
sphere_restaurant_app = SphereRestaurantApp()

# Hire some waiters
print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "John", 40))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 20))
print(sphere_restaurant_app.hire_waiter("InvalidWaiter", "JohnDoe", 10))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Charlie", 30))
print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "Frank", 50))
print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 60))

# Admit some clients
print(sphere_restaurant_app.admit_client("InvalidClient", "JohnDoe"))
print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
print(sphere_restaurant_app.admit_client("VIPClient", "Lila"))
print(sphere_restaurant_app.admit_client("RegularClient", "Bob"))
print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
print(sphere_restaurant_app.admit_client("RegularClient", "Oscar"))

# Process shifts
print(sphere_restaurant_app.process_shifts("John"))
print(sphere_restaurant_app.process_shifts("Alice"))
print(sphere_restaurant_app.process_shifts("Emily"))
print(sphere_restaurant_app.process_shifts("Frank"))

# Process client orders
print(sphere_restaurant_app.process_client_order("Bob", 100.0))
print(sphere_restaurant_app.process_client_order("Eve", 500.0))
print(sphere_restaurant_app.process_client_order("JohnDoe", 250.0))
print(sphere_restaurant_app.process_client_order("Bob", 750.0))
print(sphere_restaurant_app.process_client_order("Lila", 550.0))
print(sphere_restaurant_app.process_client_order("Oscar", 84.0))

# Apply discounts to clients
print(sphere_restaurant_app.apply_discount_to_client("Lila"))
print(sphere_restaurant_app.apply_discount_to_client("Eve"))
print(sphere_restaurant_app.apply_discount_to_client("JohnDoe"))
print(sphere_restaurant_app.apply_discount_to_client("Oscar"))
print(sphere_restaurant_app.apply_discount_to_client("Bob"))

# Generate report
print(sphere_restaurant_app.generate_report())
