from typing import List

from project_02.dvd import DVD
from project_02.customer import Customer


class MovieWorld:

    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < 10:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):

        client = [customer for customer in self.customers if customer.id == customer_id][0]
        wanted_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if wanted_dvd in client.rented_dvds:
            return f"{client.name} has already rented {wanted_dvd.name}"
        elif wanted_dvd.is_rented:
            return "DVD is already rented"
        elif client.age <= wanted_dvd.age_restriction:
            return f"{client.name} should be at least {wanted_dvd.age_restriction} to rent this movie"
        else:
            client.rented_dvds.append(wanted_dvd)
            wanted_dvd.is_rented = True
            return f"{client.name} has successfully rented {wanted_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        client = [customer for customer in self.customers if customer.id == customer_id][0]
        returning_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if returning_dvd in client.rented_dvds:
            client.rented_dvds.remove(returning_dvd)
            returning_dvd.is_rented = False
            return f"{client.name} has successfully returned {returning_dvd.name}"
        return f"{client.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += customer.__repr__() + '\n'
        for dvd in self.dvds:
            result += dvd.__repr__() + '\n'

        return result


# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
#
# print(movie_world)
