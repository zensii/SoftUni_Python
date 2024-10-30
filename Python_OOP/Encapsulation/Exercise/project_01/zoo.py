from project_01.animal import Animal


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list = []
        self.workers: list = []


    def add_animal(self, animal: Animal, price: int):
        if len(self.animals) < self.__animal_capacity:
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            self.workers.remove(next(worker for worker in self.workers if worker.name == worker_name))
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_cash = sum([worker.salary for worker in self.workers])
        if needed_cash <= self.__budget:
            self.__budget -= needed_cash
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_cash = sum([animal.money_for_care for animal in self.animals])
        if needed_cash <= self.__budget:
            self.__budget -= needed_cash
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        return (f"You have {len(self.animals)} animals\n" +
                f"----- {len([animal for animal in self.animals if animal.__class__.__name__ == 'Lion'])} Lions:\n" +
                f"{chr(10).join([animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Lion'])}" +
                f"\n----- {len([animal for animal in self.animals if animal.__class__.__name__ == 'Tiger'])} Tigers:\n" +
                f"{chr(10).join([animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Tiger'])}" +
                f"\n----- {len([animal for animal in self.animals if animal.__class__.__name__ == 'Cheetah'])} Cheetahs:\n" +
                f"{chr(10).join([animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Cheetah'])}")


    def workers_status(self):

        worker_types = ['Keeper', 'Caretaker', 'Vet']
        status_lines = [f"You have {len(self.workers)} workers"]

        for worker_type in worker_types:
            total_of_type = [worker for worker in self.workers if worker.__class__.__name__ == worker_type]
            status_lines.append(f"----- {len(total_of_type)} {worker_type}s:")
            for each in total_of_type:
                status_lines.append(each.__repr__())

        return '\n'.join(status_lines)


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
