from typing import List

from project_04.customer import Customer
from project_04.equipment import Equipment
from project_04.exercise_plan import ExercisePlan
from project_04.subscription import Subscription
from project_04.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    @staticmethod
    def find_object(name: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == name:
                return obj

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subs = [sub for sub in self.subscriptions if sub.id == subscription_id][0]
        cust = [cust for cust in self.customers if cust.id == subs.customer_id][0]
        train = [train for train in self.trainers if train.id == subs.trainer_id][0]
        pln = [pln for pln in self.plans if pln.equipment_id == subs.exercise_id][0]
        equip = [equip for equip in self.equipment if equip.id == pln.exercise_id][0]

        return f"{subs.__repr__()}\n{cust.__repr__()}\n{train.__repr__()}\n{equip.__repr__()}\n{pln.__repr__()}"


# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))
